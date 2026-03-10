class PromptTemplates:
    def build_reasoning_prompt(self, question):
        return (
            f"Question: {question}\n\n"
            "Respond using exactly this format:\n"
            "Premise: ...\n"
            "Rule: ...\n"
            "Conclusion: ..."
        )
