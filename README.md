# tool-router-lite

规则式**工具意图路由**：把用户 query 分类到天气/计算/搜索/文件/闲聊等意图，
基于关键词命中打分，输出意图与置信度。零第三方依赖。

## 功能简介

- 内置 5 类意图：weather / calculator / search / file / chat；
- `route(query)` 返回 `{intent, confidence, scores}`；
- 无任何关键词命中时返回 `unknown`，置信度 0。

## 快速开始

```bash
python3 tool_router.py "今天北京天气怎么样"
python3 tool_router.py "帮我计算 12 乘以 8"
```

作为库：

```python
from tool_router import route
print(route("搜索一下量子计算机")["intent"])
```

## 无 API key 如何运行

纯规则，**不需要任何 API key**。

## 目录结构

```
tool-router-lite/
├── tool_router.py
├── tests/test_tool_router.py
├── README.md / LICENSE / .gitignore
```

## 运行测试

```bash
python3 -m unittest discover -s tests -v
```

## 许可证

[MIT](./LICENSE) © 2026 ljiang9
