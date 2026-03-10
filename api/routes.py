from api.schema import ReasoningResponse
from extractor.reasoning_extractor import ReasoningExtractor
from governance.eal_engine import EALEngine
from knowledge.knowledge_base import KnowledgeBase
from llm.reasoning_generator import ReasoningGenerator
from trace.trace_generator import TraceGenerator


def process_question(question):
    generator = ReasoningGenerator()
    extractor = ReasoningExtractor()
    engine = EALEngine()
    tracer = TraceGenerator()
    kb = KnowledgeBase()

    tracer.start_trace()

    reasoning_text = generator.generate_reasoning(question)
    tracer.add_step("Generated reasoning text.")

    graph = extractor.extract_graph(reasoning_text)
    tracer.add_step("Extracted AIR graph from reasoning text.")

    conclusions = [node.value for node in graph.get_conclusions()]

    rules = []
    for node in graph.get_rules():
        rules.append(
            {
                "name": node.value,
                "conditions": [],
                "conclusion": conclusions[0] if conclusions else None,
                "priority": 1,
                "type": "general",
            }
        )

    tracer.add_step(f"Extracted {len(rules)} rules from AIR graph.")

    result = engine.evaluate(kb, rules)
    tracer.add_step(f"Evaluated rules with EALEngine: {result.get('status')}.")

    trace = tracer.get_trace()

    return ReasoningResponse(
        status=result.get("status"),
        rule=result.get("rule"),
        trace=trace,
    )