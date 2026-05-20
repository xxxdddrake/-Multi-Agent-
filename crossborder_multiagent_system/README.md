# Cross-Border E-commerce Multi-Agent System

一个基于 FastAPI + LangChain 风格架构 的跨境电商多智能体（Multi-Agent）智能出海运营系统。

## 功能模块

- 市场分析 Agent
- 商品选品 Agent
- SEO 内容 Agent
- 广告投放 Agent
- 客服 Agent
- 数据分析 Agent
- 工作流编排
- REST API
- Docker 支持

## 技术栈

- Python 3.11
- FastAPI
- Uvicorn
- Pydantic
- AsyncIO

## 启动方式

```bash
pip install -r requirements.txt
python main.py
```

访问：

http://127.0.0.1:8000/docs

## API 示例

POST /run-workflow

```json
{
  "product": "智能蓝牙耳机",
  "market": "美国"
}
```

## 推荐后续升级

- 接入 OpenAI / DeepSeek API
- 接入 PostgreSQL
- 接入 Redis
- 加入 AutoGen / CrewAI
- 加入 RAG 知识库
- 加入 Shopify / TikTok Shop API