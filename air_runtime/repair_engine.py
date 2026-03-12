class RepairEngine:
    def suggest(self, failure):
        error_type = failure.get("error_type") if isinstance(failure, dict) else None

        if error_type == "missing_premise":
            repair_type = "add_premise"
            suggestion = "Add supporting premise or evidence for this rule."
        elif error_type == "invalid_rule":
            repair_type = "fix_rule"
            suggestion = "Rewrite the reasoning rule so it contains a valid operator."
        else:
            repair_type = "review_reasoning"
            suggestion = "Review reasoning step for logical consistency."

        return {
            "repair_type": repair_type,
            "suggestion": suggestion,
            "step_id": failure.get("step_id") if isinstance(failure, dict) else None,
        }
