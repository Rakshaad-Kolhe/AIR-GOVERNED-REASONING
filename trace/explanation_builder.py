class ExplanationBuilder:
    def build_explanation(self, result):
        status = str(result.get("status", "UNKNOWN"))
        rule = result.get("rule")
        trace = result.get("trace", [])

        status_text = f"The system {status}ED the inference"
        if rule:
            status_text += f" using rule '{rule}'."
        else:
            status_text += "."

        if trace:
            steps_text = " \u2192 ".join(str(step) for step in trace)
            return f"{status_text} Reasoning steps: {steps_text}"

        return f"{status_text} Reasoning steps: none."
