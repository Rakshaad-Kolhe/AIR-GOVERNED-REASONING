class ConstraintSolver:
    def check(self, step):
        if not step.operator:
            return False

        if not step.premises:
            return False

        return True
