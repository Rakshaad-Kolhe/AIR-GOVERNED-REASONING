class ConstraintGeneralizer:
    def __init__(self):
        self.mapping = {
            "hypertension": "medical_condition",
            "smoking": "risk_factor",
            "aspirin": "medication",
        }

    def generalize(self, constraint):
        premises = constraint.get("premises", [])
        generalized_premises = [self.mapping.get(premise, premise) for premise in premises]

        return {
            "premises": generalized_premises,
            "operator": constraint.get("operator"),
            "required_relation": constraint.get("required_relation"),
        }
