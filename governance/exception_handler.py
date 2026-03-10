class ExceptionHandler:
    def is_exception(self, rule):
        return rule.get("type") == "exception"

    def check_exception(self, kb, rule, exception_rules):
        for exception_rule in exception_rules:
            if not self.is_exception(exception_rule):
                continue

            conditions = exception_rule.get("conditions", [])
            if all(kb.has_fact(condition) for condition in conditions):
                return exception_rule

        return None
