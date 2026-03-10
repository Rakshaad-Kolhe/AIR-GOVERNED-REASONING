from air.edge import Edge
from air.graph import AIRGraph
from air.node import Node
from extractor.conclusion_detector import ConclusionDetector
from extractor.premise_detector import PremiseDetector
from extractor.rule_detector import RuleDetector


class ReasoningExtractor:
    def __init__(self):
        self.premise_detector = PremiseDetector()
        self.rule_detector = RuleDetector()
        self.conclusion_detector = ConclusionDetector()

    def extract_graph(self, text):
        premises = self.premise_detector.extract(text)
        rules = self.rule_detector.extract(text)
        conclusions = self.conclusion_detector.extract(text)

        graph = AIRGraph()

        premise_ids = []
        for index, premise in enumerate(premises, start=1):
            node_id = f"p{index}"
            graph.add_node(Node(node_id=node_id, node_type="premise", value=premise))
            premise_ids.append(node_id)

        rule_ids = []
        for index, rule in enumerate(rules, start=1):
            node_id = f"r{index}"
            graph.add_node(Node(node_id=node_id, node_type="rule", value=rule))
            rule_ids.append(node_id)

        conclusion_ids = []
        for index, conclusion in enumerate(conclusions, start=1):
            node_id = f"c{index}"
            graph.add_node(Node(node_id=node_id, node_type="conclusion", value=conclusion))
            conclusion_ids.append(node_id)

        for premise_id in premise_ids:
            for rule_id in rule_ids:
                graph.add_edge(Edge(source=premise_id, target=rule_id))

        for rule_id in rule_ids:
            for conclusion_id in conclusion_ids:
                graph.add_edge(Edge(source=rule_id, target=conclusion_id))

        return graph
