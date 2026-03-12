from api.schema import ReasoningResponse
from air_ir.ir_builder import AIRIRBuilder
from air_ir.ir_executor import AIRExecutor
from extractor.reasoning_extractor import ReasoningExtractor
from knowledge.knowledge_base import KnowledgeBase
from llm.reasoning_generator import ReasoningGenerator
from trace.trace_generator import TraceGenerator


def process_question(question):
    generator = ReasoningGenerator()
    extractor = ReasoningExtractor()
    builder = AIRIRBuilder()
    executor = AIRExecutor()
    tracer = TraceGenerator()
    kb = KnowledgeBase()

    tracer.start_trace()

    reasoning_text = generator.generate_reasoning(question)
    tracer.add_step("Generated reasoning text.")

    graph = extractor.extract_graph(reasoning_text)
    tracer.add_step("Extracted AIR graph from reasoning text.")

    steps = builder.build(graph)

    tracer.add_step(f"Extracted {len(steps)} rules from AIR graph.")

    result = executor.execute(kb, steps)
    tracer.add_step(f"Evaluated rules with EALEngine: {result.get('status')}.")

    trace = tracer.get_trace()

    return ReasoningResponse(
        status=result.get("status"),
        rule=result.get("rule"),
        trace=trace,
    )
