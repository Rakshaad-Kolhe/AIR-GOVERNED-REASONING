from llm.llm_interface import LLMInterface
from llm.prompt_templates import PromptTemplates


class ReasoningGenerator:
    def __init__(self):
        self.llm = LLMInterface()
        self.templates = PromptTemplates()

    def generate_reasoning(self, question):
        prompt = self.templates.build_reasoning_prompt(question)
        reasoning = self.llm.generate(prompt)
        return reasoning
