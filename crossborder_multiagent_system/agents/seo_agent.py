from agents.base_agent import BaseAgent

class SEOAgent(BaseAgent):

    def __init__(self):
        super().__init__("SEOAgent")

    async def run(self, data):
        return {
            "keywords": [
                data["product"],
                "best seller",
                "amazon hot"
            ],
            "description": f"{data['product']} 高转化 SEO 描述"
        }