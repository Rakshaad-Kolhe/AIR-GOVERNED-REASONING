class TraceGraph:
    def __init__(self):
        self.nodes = []

    def add_step(self, step, result):
        node = {
            "step_id": step.step_id,
            "premises": step.premises,
            "rule": step.operator,
            "conclusion": step.conclusion,
            "status": result.get("status") if isinstance(result, dict) else None,
            "failure": result.get("failure") if isinstance(result, dict) else None,
        }
        self.nodes.append(node)

    def get_trace(self):
        return self.nodes

    def to_dict(self):
        return {
            "reasoning_trace": self.nodes,
        }
