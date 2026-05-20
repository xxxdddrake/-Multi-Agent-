from agents.base_agent import BaseAgent

class CustomerServiceAgent(BaseAgent):

    def __init__(self):
        super().__init__("CustomerServiceAgent")

    async def run(self, data):
        return {
            "reply_template": f"感谢您购买 {data['product']}，我们将尽快发货。"
        }