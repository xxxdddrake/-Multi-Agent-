class BaseAgent:
    def __init__(self, name):
        self.name = name

    async def run(self, data):
        raise NotImplementedError