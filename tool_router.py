#!/usr/bin/env python3
"""tool_router —— 规则式工具意图路由。

把用户 query 分类到若干意图（天气/计算/搜索/文件/闲聊等），
基于关键词命中打分，输出最可能意图与置信度。零第三方依赖。

用法：
    from tool_router import route
    print(route("今天北京天气怎么样"))
"""
from __future__ import annotations

import argparse
import re
import sys

INTENTS = {
    "weather": ["天气", "气温", "下雨", "温度", "晴", "预报", "weather", "rain", "temperature"],
    "calculator": ["计算", "等于", "加", "减", "乘", "除以", "+", "*", "多少", "calculate"],
    "search": ["搜索", "查一下", "百度", "谷歌", "资料", "是什么", "search", "find"],
    "file": ["文件", "保存", "读取", "删除", "目录", "写", "file", "save", "read"],
    "chat": ["你好", "谢谢", "再见", "你是谁", "hi", "hello", "thanks"],
}


def route(query: str) -> dict:
    q = query.lower()
    scores = {}
    for intent, kws in INTENTS.items():
        hits = sum(1 for kw in kws if kw.lower() in q)
        scores[intent] = hits
    total = sum(scores.values())
    best = max(scores, key=scores.get)
    conf = (scores[best] / total) if total > 0 else 0.0
    return {
        "query": query,
        "intent": best if total > 0 else "unknown",
        "confidence": round(conf, 3),
        "scores": scores,
    }


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="工具意图路由")
    p.add_argument("query", nargs="?", help="用户 query；不传则读标准输入")
    args = p.parse_args(argv)
    q = args.query or sys.stdin.read()
    r = route(q)
    print(f"意图：{r['intent']}（置信度 {r['confidence']:.2f}）")
    for k, v in sorted(r["scores"].items(), key=lambda kv: -kv[1]):
        print(f"  {k}\t命中 {v}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
