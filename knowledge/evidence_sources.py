class EvidenceStore:
    ALLOWED_SOURCES = {"perception", "inference", "testimony", "unknown"}

    def __init__(self):
        self.sources = {}

    def set_source(self, fact, source):
        fact_key = str(fact)
        source_value = str(source)
        if source_value not in self.ALLOWED_SOURCES:
            raise ValueError(
                f"Invalid source '{source_value}'. Allowed sources: {sorted(self.ALLOWED_SOURCES)}"
            )
        self.sources[fact_key] = source_value

    def get_source(self, fact):
        return self.sources.get(str(fact), "unknown")

    def has_source(self, fact):
        return str(fact) in self.sources

    def remove_source(self, fact):
        self.sources.pop(str(fact), None)

    def get_all_sources(self):
        return dict(self.sources)
