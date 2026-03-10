from .evidence_sources import EvidenceStore
from .fact_store import FactStore


class KnowledgeBase:
    def __init__(self):
        self.fact_store = FactStore()
        self.evidence_store = EvidenceStore()

    def add_fact(self, fact, source="unknown"):
        self.fact_store.add_fact(fact)
        self.evidence_store.set_source(fact, source)

    def remove_fact(self, fact):
        self.fact_store.remove_fact(fact)
        self.evidence_store.remove_source(fact)

    def has_fact(self, fact):
        return self.fact_store.has_fact(fact)

    def get_source(self, fact):
        return self.evidence_store.get_source(fact)

    def get_all_facts(self):
        return self.fact_store.get_all_facts()

    def get_all_sources(self):
        return self.evidence_store.get_all_sources()
