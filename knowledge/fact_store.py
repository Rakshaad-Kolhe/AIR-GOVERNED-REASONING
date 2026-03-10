class FactStore:
    def __init__(self):
        self.facts = set()

    def add_fact(self, fact):
        self.facts.add(str(fact))

    def remove_fact(self, fact):
        self.facts.discard(str(fact))

    def has_fact(self, fact):
        return str(fact) in self.facts

    def get_all_facts(self):
        return list(self.facts)

    def clear(self):
        self.facts.clear()
