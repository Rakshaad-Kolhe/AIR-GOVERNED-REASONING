import json


def serialize_graph(graph):
    return graph.to_dict()


def graph_to_json(graph):
    return json.dumps(serialize_graph(graph), indent=2)


def save_graph(graph, filepath):
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(serialize_graph(graph), f, indent=2)
