from air_ir.ir_step import AIRStep


class AIRIRBuilder:
    def build(self, graph):
        premises = graph.get_premises() or []
        rules = graph.get_rules() or []
        conclusions = graph.get_conclusions() or []

        premise_values = [self._node_value(p) for p in premises]
        conclusion_value = self._node_value(conclusions[0]) if conclusions else ""

        steps = []
        for index, rule in enumerate(rules, start=1):
            step = AIRStep(
                step_id=f"s{index}",
                premises=premise_values,
                operator=self._node_value(rule),
                conclusion=conclusion_value,
                evidence=[],
                priority=1,
                exceptions=[],
                status="proposed",
            )
            steps.append(step)

        return steps

    @staticmethod
    def _node_value(node):
        if node is None:
            return ""

        if hasattr(node, "value"):
            value = getattr(node, "value")
            return "" if value is None else str(value)

        if isinstance(node, dict) and "value" in node:
            value = node.get("value")
            return "" if value is None else str(value)

        return str(node)
