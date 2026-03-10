class RulePrioritizer:
    def sort_rules(self, rules):
        return sorted(rules, key=lambda rule: rule.get("priority", 0), reverse=True)
