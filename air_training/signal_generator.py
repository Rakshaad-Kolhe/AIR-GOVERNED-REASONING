class TrainingSignalGenerator:
    def generate(self, question, result):
        if result.get("status") != "REJECT":
            return None

        failure = result.get("failure")
        repair = result.get("repair")
        constraint = result.get("constraint")

        return {
            "question": question,
            "failure_type": failure.get("error_type") if failure else None,
            "repair_suggestion": repair.get("suggestion") if repair else None,
            "trace": result.get("reasoning_trace"),
            "constraint": constraint,
        }
