import json
import os


class ConstraintLibrary:
    def __init__(self):
        self.storage_file = "constraints.json"
        self.constraints = []
        self.hierarchy = {
            "hypertension": "medical_condition",
            "smoking": "risk_factor",
            "aspirin": "medication",
        }

        if os.path.exists(self.storage_file):
            try:
                with open(self.storage_file, "r") as f:
                    loaded = json.load(f)
                self.constraints = loaded if isinstance(loaded, list) else []
            except Exception:
                self.constraints = []

    def add(self, constraint):
        if constraint is not None:
            self.constraints.append(constraint)
            try:
                with open(self.storage_file, "w") as f:
                    json.dump(self.constraints, f, indent=2)
            except Exception:
                pass

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

    def get_statistics(self):
        statistics = {}

        for constraint in self.constraints:
            if not isinstance(constraint, dict):
                continue

            required_relation = constraint.get("required_relation")
            if required_relation is None:
                continue

            statistics[required_relation] = statistics.get(required_relation, 0) + 1

        return statistics
