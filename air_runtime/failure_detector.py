class FailureDetector:
    def detect(self, step, result):
        if not isinstance(result, dict) or result.get("status") != "REJECT":
            return None

        if not getattr(step, "premises", []):
            error_type = "missing_premise"
        elif not getattr(step, "operator", ""):
            error_type = "invalid_rule"
        else:
            error_type = "unknown"

        return {
            "error_type": error_type,
            "step_id": getattr(step, "step_id", ""),
            "operator": getattr(step, "operator", ""),
        }
