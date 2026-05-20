from agents.base_agent import BaseAgent

class MarketAgent(BaseAgent):

    def __init__(self):
        super().__init__("MarketAgent")

    async def run(self, data):
        return {
            "market_trend": f"{data['market']} 市场对 {data['product']} 需求增长明显",
            "competition": "中等竞争"
        }