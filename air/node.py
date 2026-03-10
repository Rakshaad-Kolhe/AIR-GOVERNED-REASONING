class Node:
    VALID_TYPES = {"premise", "rule", "conclusion"}

    def __init__(self, node_id, node_type, value, metadata=None):
        if node_type not in self.VALID_TYPES:
            raise ValueError(
                f"Invalid node type: {node_type}. Must be one of: premise, rule, conclusion."
            )

        self.id = str(node_id)
        self.type = str(node_type)
        self.value = str(value)
        self.metadata = metadata if metadata is not None else {}

    def to_dict(self):
        return {
            "id": self.id,
            "type": self.type,
            "value": self.value,
            "metadata": self.metadata,
        }

    def __repr__(self):
        return (
            "Node(\n"
            f' id="{self.id}",\n'
            f' type="{self.type}",\n'
            f' value="{self.value}"\n'
            ")"
        )
