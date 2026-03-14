class ReasoningVerifier:
    def __init__(self, extractor, builder, executor):
        self.extractor = extractor
        self.builder = builder
        self.executor = executor

    def verify(self, reasoning_text, kb):
        graph = self.extractor.extract_graph(reasoning_text)
        steps = self.builder.build(graph)
        return self.executor.execute(kb, steps)
