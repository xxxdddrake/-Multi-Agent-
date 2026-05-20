from agents.base_agent import BaseAgent

class ProductAgent(BaseAgent):

    def __init__(self):
        super().__init__("ProductAgent")

    async def run(self, data):
        return {
            "recommended_title": f"{data['product']} Pro Max",
            "price_strategy": "39.99 USD"
        }