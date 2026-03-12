class AIRStep:
    def __init__(
        self,
        step_id,
        premises=None,
        operator="",
        conclusion="",
        evidence=None,
        priority=1,
        exceptions=None,
        status="proposed",
    ):
        self.step_id = str(step_id) if step_id is not None else "s0"
        self.premises = self._to_string_list(premises)
        self.operator = "" if operator is None else str(operator)
        self.conclusion = "" if conclusion is None else str(conclusion)
        self.evidence = self._to_evidence_list(evidence)
        self.priority = self._to_int(priority, default=1)
        self.exceptions = self._to_list(exceptions)
        self.status = "proposed" if status is None else str(status)

    @staticmethod
    def _to_int(value, default=1):
        try:
            return int(value)
        except (TypeError, ValueError):
            return default

    @staticmethod
    def _to_string_list(value):
        if value is None:
            return []
        if isinstance(value, (list, tuple, set)):
            return ["" if item is None else str(item) for item in value]
        return [str(value)]

    @staticmethod
    def _to_list(value):
        if value is None:
            return []
        if isinstance(value, (list, tuple, set)):
            return list(value)
        return [value]

    @staticmethod
    def _to_evidence_list(value):
        if value is None:
            return []
        if not isinstance(value, (list, tuple, set)):
            value = [value]

        evidence_list = []
        for item in value:
            if isinstance(item, dict):
                evidence_list.append(dict(item))
            else:
                evidence_list.append({"value": item})
        return evidence_list

    def to_rule(self):
        return {
            "name": self.operator,
            "conditions": self.premises,
            "conclusion": self.conclusion,
            "priority": self.priority,
            "type": "general",
        }

    def to_dict(self):
        return {
            "step_id": self.step_id,
            "premises": self.premises,
            "operator": self.operator,
            "conclusion": self.conclusion,
            "evidence": self.evidence,
            "priority": self.priority,
            "exceptions": self.exceptions,
            "status": self.status,
        }

    def __repr__(self):
        return (
            "AIRStep(\n"
            f' step_id="{self.step_id}",\n'
            f" premises={self.premises},\n"
            f' operator="{self.operator}",\n'
            f' conclusion="{self.conclusion}",\n'
            f" evidence={self.evidence},\n"
            f" priority={self.priority},\n"
            f" exceptions={self.exceptions},\n"
            f' status="{self.status}"\n'
            ")"
        )
