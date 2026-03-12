class ReasoningSupervisor:
    def __init__(self, generator, extractor, builder, executor):
        self.generator = generator
        self.extractor = extractor
        self.builder = builder
        self.executor = executor

    def run(self, question, kb, max_attempts=3):
        prompt = question
        last_result = None

        for _ in range(max_attempts):
            reasoning_text = self.generator.generate_reasoning(prompt)
            graph = self.extractor.extract_graph(reasoning_text)
            steps = self.builder.build(graph)
            result = self.executor.execute(kb, steps)
            last_result = result

            if result["status"] != "REJECT":
                return result

            repair = result.get("repair")
            if repair:
                suggestion = repair["suggestion"]
                prompt = prompt + "\nRepair suggestion: " + suggestion

        return last_result
