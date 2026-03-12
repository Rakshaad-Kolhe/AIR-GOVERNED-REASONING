class ReasoningLoop:
    def __init__(self, generator, extractor, builder, executor):
        self.generator = generator
        self.extractor = extractor
        self.builder = builder
        self.executor = executor

    def run(self, question, kb, max_attempts=3):
        prompt = str(question)
        final_result = {
            "status": "SUSPEND",
            "rule": None,
            "steps_evaluated": 0,
            "failure": None,
            "repair": None,
        }

        for _ in range(max_attempts):
            reasoning_text = self.generator.generate_reasoning(prompt)
            graph = self.extractor.extract_graph(reasoning_text)
            steps = self.builder.build(graph)
            result = self.executor.execute(kb, steps)
            final_result = result

            if result.get("status") != "REJECT":
                return result

            repair = result.get("repair") if isinstance(result, dict) else None
            suggestion = repair.get("suggestion") if isinstance(repair, dict) else None
            if suggestion:
                prompt = f"{prompt}\nRepair suggestion: {suggestion}"

        return final_result
