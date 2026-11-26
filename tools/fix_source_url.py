#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""修复 source_url 插错位置：从文末移到 front-matter 结束符前（幂等）"""
import glob
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
POSTS = os.path.join(ROOT, "source", "_posts")

fixed = 0
ok = 0

for path in glob.glob(os.path.join(POSTS, "*.md")):
    name = os.path.basename(path)
    if not re.match(r"^\d+-", name):
        continue

    with open(path, encoding="utf-8") as f:
        lines = f.read().split("\n")

    # 找到文末错插的 source_url 行（在第 2 行之后出现的）
    err_idx = None
    for i in range(1, len(lines)):
        if lines[i].startswith("source_url:"):
            err_idx = i
            source_line = lines[i]
            break

    if err_idx is None:
        # 检查是否已在正确位置（front-matter 内，即前 20 行）
        fm_end = next((i for i in range(1, 20) if lines[i].strip() == "---"), None)
        if fm_end and any("source_url:" in l for l in lines[1:fm_end]):
            ok += 1
        else:
            print(f"WARN 无 source_url: {name}")
        continue

    # 是否已经在 front-matter 内？
    fm_end = next((i for i in range(1, 20) if lines[i].strip() == "---"), None)
    if fm_end and err_idx < fm_end:
        ok += 1
        continue

    # 移除错插的行
    lines.pop(err_idx)

    # 重新计算 front-matter 结束符（第 2 个 --- ，在开头 --- 之后）
    fm_end = next((i for i in range(1, 20) if lines[i].strip() == "---"), None)
    if fm_end is None:
        print(f"WARN 无 front-matter 结束符: {name}")
        continue

    lines.insert(fm_end, source_line)

    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    fixed += 1

print(f"修复: {fixed} 篇，已正确: {ok} 篇")
