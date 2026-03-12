from governance.eal_engine import EALEngine


class AIRExecutor:
    def __init__(self):
        self.engine = EALEngine()

    def execute(self, kb, steps):
        steps = steps or []
        if not steps:
            return {
                "status": "SUSPEND",
                "rule": None,
                "steps_evaluated": 0,
            }

        steps_evaluated = 0
        final_result = None

        for step in steps:
            rule = step.to_rule()
            result = self.engine.evaluate(kb, [rule])
            steps_evaluated += 1
            final_result = result

            if result.get("status") == "REJECT":
                return {
                    "status": result.get("status"),
                    "rule": result.get("rule"),
                    "steps_evaluated": steps_evaluated,
                }

        return {
            "status": final_result.get("status") if final_result else "SUSPEND",
            "rule": final_result.get("rule") if final_result else None,
            "steps_evaluated": steps_evaluated,
        }
