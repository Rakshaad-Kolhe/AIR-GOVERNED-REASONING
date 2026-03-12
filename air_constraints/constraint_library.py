class ConstraintLibrary:
    def __init__(self):
        self.constraints = []

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
                if premise in constraint_premises:
                    matches.append(constraint)
                    break

        return matches
