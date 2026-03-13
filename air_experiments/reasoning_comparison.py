class ReasoningComparison:
    def __init__(self, supervisor, kb):
        self.supervisor = supervisor
        self.kb = kb

    def run(self, questions):
        baseline_accept = 0
        baseline_reject = 0
        air_accept = 0
        air_reject = 0

        for question in questions:
            baseline_result = "ACCEPT"
            if baseline_result == "ACCEPT":
                baseline_accept += 1
            else:
                baseline_reject += 1

            result = self.supervisor.run(question, self.kb)
            if result.get("status") == "ACCEPT":
                air_accept += 1
            else:
                air_reject += 1

        return {
            "baseline": {
                "accept": baseline_accept,
                "reject": baseline_reject,
            },
            "air": {
                "accept": air_accept,
                "reject": air_reject,
            },
        }
