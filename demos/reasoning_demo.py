from air_analytics.constraint_stats import ConstraintStats
from air_constraints.constraint_library import ConstraintLibrary
from air_evaluation.metrics import AIRMetrics
from air_evaluation.verifier_benchmark import VerifierBenchmark
from air_experiments.reasoning_comparison import ReasoningComparison
from air_ir.ir_builder import AIRIRBuilder
from air_ir.ir_executor import AIRExecutor
from air_runtime.reasoning_supervisor import ReasoningSupervisor
from extractor.reasoning_extractor import ReasoningExtractor
from knowledge.knowledge_base import KnowledgeBase
from llm.reasoning_generator import ReasoningGenerator


def main():
    generator = ReasoningGenerator()
    extractor = ReasoningExtractor()
    builder = AIRIRBuilder()
    executor = AIRExecutor()

    supervisor = ReasoningSupervisor(generator, extractor, builder, executor)

    kb = KnowledgeBase()
    kb.add_fact("Hypertension can increase cardiovascular risk.", source="medical_guideline")
    kb.add_fact("Smoking is linked to lung cancer risk.", source="medical_guideline")
    kb.add_fact("Aspirin may reduce heart attack risk in some cases.", source="clinical_evidence")

    question = "Should hypertension be treated?"
    result = supervisor.run(question, kb)

    print("AIR Reasoning Demo Result:")
    print(result)

    metrics = AIRMetrics()
    benchmark = VerifierBenchmark(supervisor, kb, metrics)

    questions = [
        "Should hypertension be treated?",
        "Does smoking cause lung cancer?",
        "Can aspirin prevent heart attack?",
    ]

    results = benchmark.run(questions)

    print("AIR Benchmark Results:")
    print(results)

    comparison = ReasoningComparison(supervisor, kb)
    comparison_results = comparison.run(questions)
    print("AIR Reasoning Comparison:")
    print(comparison_results)

    constraint_library = ConstraintLibrary()
    stats = ConstraintStats(constraint_library)
    stats.print_report()


if __name__ == "__main__":
    main()
