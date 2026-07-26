class Pipeline:

    def __init__(self):
        self.steps = []

    def add(self, func):
        self.steps.append(func)

    async def run(self):
        for step in self.steps:
            await step()
