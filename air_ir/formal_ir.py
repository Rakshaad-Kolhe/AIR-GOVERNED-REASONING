class FormalAIRStep:
    def __init__(self, premises, operator, conclusion, evidence=None):
        self.premises = premises or []
        self.operator = operator
        self.conclusion = conclusion
        self.evidence = evidence or []

    def tuple(self):
        return (self.premises, self.operator, self.conclusion, self.evidence)

    def to_dict(self):
        return {
            "premises": self.premises,
            "operator": self.operator,
            "conclusion": self.conclusion,
            "evidence": self.evidence,
        }
