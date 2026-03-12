class AIRKernel:
    def __init__(self, constraint_solver, policy_engine, eal_engine):
        self.constraint_solver = constraint_solver
        self.policy_engine = policy_engine
        self.eal_engine = eal_engine

    def process(self, step, kb):
        if not self.constraint_solver.check(step):
            return {"status": "REJECT", "reason": "constraint_failed"}

        if not self.policy_engine.check(step):
            return {"status": "REJECT", "reason": "policy_failed"}

        rule = step.to_rule()
        result = self.eal_engine.evaluate(kb, [rule])
        return result
