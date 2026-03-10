class TraceGenerator:
    def __init__(self):
        self.steps = []

    def start_trace(self):
        self.steps = []

    def add_step(self, message):
        self.steps.append(str(message))

    def get_trace(self):
        return list(self.steps)

    def build_result(self, status, rule_name=None):
        return {
            "status": status,
            "rule": rule_name,
            "trace": self.get_trace(),
        }
