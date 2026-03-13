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

    def print_report(self, results):
        baseline_accept = results["baseline"]["accept"]
        baseline_reject = results["baseline"]["reject"]

        air_accept = results["air"]["accept"]
        air_reject = results["air"]["reject"]

        baseline_total = baseline_accept + baseline_reject
        air_total = air_accept + air_reject

        improvement = (air_reject / air_total) * 100 if air_total else 0

        print("AIR Reasoning Comparison")
        print("")
        print("System        Accept   Reject")
        print("--------------------------------")
        print(f"LLM baseline   {baseline_accept}       {baseline_reject}")
        print(f"LLM + AIR      {air_accept}       {air_reject}")
        print("")
        print(
            f"AIR rejected {round(improvement, 1)}% of reasoning attempts that baseline would accept."
        )
