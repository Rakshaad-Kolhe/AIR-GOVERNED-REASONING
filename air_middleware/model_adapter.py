class ModelAdapter:
    def __init__(self, generator):
        self.generator = generator

    def generate_reasoning(self, question):
        return self.generator.generate_reasoning(question)
