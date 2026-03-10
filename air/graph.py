class AIRGraph:
    def __init__(self):
        self.nodes = {}
        self.edges = []

    def add_node(self, node):
        node_id = str(node.id)
        if node_id in self.nodes:
            raise ValueError(f"Node with id '{node_id}' already exists.")
        self.nodes[node_id] = node

    def add_edge(self, edge):
        self.edges.append(edge)

    def get_node(self, node_id):
        return self.nodes.get(str(node_id))

    def get_premises(self):
        return [node for node in self.nodes.values() if getattr(node, "type", None) == "premise"]

    def get_rules(self):
        return [node for node in self.nodes.values() if getattr(node, "type", None) == "rule"]

    def get_conclusions(self):
        return [node for node in self.nodes.values() if getattr(node, "type", None) == "conclusion"]

    def to_dict(self):
        return {
            "nodes": [node.to_dict() for node in self.nodes.values()],
            "edges": [edge.to_dict() for edge in self.edges],
        }
