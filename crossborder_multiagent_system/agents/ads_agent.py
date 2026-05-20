from agents.base_agent import BaseAgent

class AdsAgent(BaseAgent):

    def __init__(self):
        super().__init__("AdsAgent")

    async def run(self, data):
        return {
            "platform": "TikTok Ads",
            "budget": "500 USD/day",
            "strategy": "短视频达人投放"
        }