from governance.eal_engine import EALEngine


class AIRExecutor:
    def __init__(self):
        self.engine = EALEngine()

    def execute(self, kb, steps):
        rules = [step.to_rule() for step in (steps or [])]
        return self.engine.evaluate(kb, rules)
