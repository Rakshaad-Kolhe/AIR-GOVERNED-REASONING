class AdmissibilityChecker:
    def check(self, step, kb):
        if step is None:
            return False

        premises = getattr(step, "premises", None) or []
        if not premises:
            return False

        for premise in premises:
            if not kb.has_fact(premise):
                return False

        return True
