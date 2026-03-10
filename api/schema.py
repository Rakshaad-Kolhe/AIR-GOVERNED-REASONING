class ReasoningRequest:
    def __init__(self, question):
        self.question = str(question)

    def to_dict(self):
        return {
            "question": self.question,
        }


class ReasoningResponse:
    def __init__(self, status, rule, trace):
        self.status = status
        self.rule = rule
        self.trace = trace

    def to_dict(self):
        return {
            "status": self.status,
            "rule": self.rule,
            "trace": self.trace,
        }
