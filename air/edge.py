class Edge:
    def __init__(self, source, target, relation="supports"):
        self.source = str(source)
        self.target = str(target)
        self.relation = str(relation)

    def to_dict(self):
        return {
            "source": self.source,
            "target": self.target,
            "relation": self.relation,
        }

    def __repr__(self):
        return (
            "Edge(\n"
            f' source="{self.source}",\n'
            f' target="{self.target}",\n'
            f' relation="{self.relation}"\n'
            ")"
        )
