class ConstraintExtractor:
    def extract(self, step, failure):
        if failure is None:
            return None

        return {
            "premises": step.premises,
            "operator": step.operator,
            "required_relation": failure.get("error_type"),
        }
