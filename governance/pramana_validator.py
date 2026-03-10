class PramanaValidator:
    STRENGTH_MAP = {
        "perception": "strong",
        "inference": "medium",
        "testimony": "medium",
        "unknown": "weak",
    }

    def get_strength(self, source):
        return self.STRENGTH_MAP.get(str(source), "weak")

    def validate_fact(self, kb, fact):
        source = kb.get_source(fact)
        strength = self.get_strength(source)
        return {
            "fact": fact,
            "source": source,
            "strength": strength,
        }
