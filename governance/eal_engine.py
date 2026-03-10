from .conflict_resolver import ConflictResolver
from .exception_handler import ExceptionHandler
from .pramana_validator import PramanaValidator
from .rule_prioritizer import RulePrioritizer


class EALEngine:
    def __init__(self):
        self.pramana_validator = PramanaValidator()
        self.exception_handler = ExceptionHandler()
        self.conflict_resolver = ConflictResolver()
        self.rule_prioritizer = RulePrioritizer()

    def applicable_rules(self, kb, rules):
        applicable = []
        for rule in rules:
            conditions = rule.get("conditions", [])
            if all(kb.has_fact(condition) for condition in conditions):
                applicable.append(rule)
        return applicable

    def evaluate(self, kb, rules):
        applicable = self.applicable_rules(kb, rules)
        if not applicable:
            return {"status": "SUSPEND", "rule": None}

        sorted_rules = self.rule_prioritizer.sort_rules(applicable)
        exception_rules = [rule for rule in rules if self.exception_handler.is_exception(rule)]

        candidate_rules = []
        for rule in sorted_rules:
            if self.exception_handler.is_exception(rule):
                continue

            blocking_rule = self.exception_handler.check_exception(kb, rule, exception_rules)
            if blocking_rule is not None:
                return {"status": "REJECT", "rule": rule.get("name")}

            candidate_rules.append(rule)

        if not candidate_rules:
            return {"status": "SUSPEND", "rule": None}

        winner = self.conflict_resolver.resolve_multiple(candidate_rules)
        if winner is None:
            return {"status": "SUSPEND", "rule": None}

        return {"status": "ACCEPT", "rule": winner.get("name")}
