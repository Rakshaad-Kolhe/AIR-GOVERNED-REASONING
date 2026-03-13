class ConstraintLibrary:
    def __init__(self):
        self.constraints = []
        self.hierarchy = {
            "hypertension": "medical_condition",
            "smoking": "risk_factor",
            "aspirin": "medication",
        }

    def add(self, constraint):
        if constraint is not None:
            self.constraints.append(constraint)

    def get_all(self):
        return list(self.constraints)

    def match(self, premises):
        matches = []
        input_premises = premises or []

        for constraint in self.constraints:
            constraint_premises = []
            if isinstance(constraint, dict):
                constraint_premises = constraint.get("premises") or []

            for premise in input_premises:
                generalized_premise = self.hierarchy.get(premise)
                if premise in constraint_premises or generalized_premise in constraint_premises:
                    matches.append(constraint)
                    break

        return matches
