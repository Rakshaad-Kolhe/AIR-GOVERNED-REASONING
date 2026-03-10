class ConflictResolver:
    def resolve(self, rule_a, rule_b):
        priority_a = rule_a.get("priority", 0)
        priority_b = rule_b.get("priority", 0)
        if priority_a > priority_b:
            return rule_a
        return rule_b

    def resolve_multiple(self, rules):
        if not rules:
            return None

        winner = rules[0]
        for rule in rules[1:]:
            winner = self.resolve(winner, rule)
        return winner
