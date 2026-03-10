class RuleDetector:
    def extract(self, text):
        rules = []
        for line in str(text).splitlines():
            stripped = line.strip()
            if stripped.startswith("Rule:"):
                rule = stripped[len("Rule:"):].strip()
                rules.append(rule)
        return rules
