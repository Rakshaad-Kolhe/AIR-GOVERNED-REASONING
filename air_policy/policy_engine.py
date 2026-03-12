class PolicyEngine:
    def check(self, step):
        if not step.conclusion:
            return False

        if not step.operator:
            return False

        return True
