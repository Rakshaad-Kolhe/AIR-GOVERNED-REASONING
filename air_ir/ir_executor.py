from governance.eal_engine import EALEngine
from air_runtime.failure_detector import FailureDetector
from air_runtime.repair_engine import RepairEngine
from air_trace.trace_graph import TraceGraph


class AIRExecutor:
    def __init__(self):
        self.engine = EALEngine()
        self.failure_detector = FailureDetector()
        self.repair_engine = RepairEngine()
        self.trace_graph = TraceGraph()

    def execute(self, kb, steps):
        self.trace_graph = TraceGraph()
        steps = steps or []
        if not steps:
            return {
                "status": "SUSPEND",
                "rule": None,
                "steps_evaluated": 0,
                "failure": None,
                "repair": None,
                "reasoning_trace": self.trace_graph.get_trace(),
            }

        steps_evaluated = 0
        final_result = None

        for step in steps:
            rule = step.to_rule()
            result = self.engine.evaluate(kb, [rule])
            self.trace_graph.add_step(step, result)
            steps_evaluated += 1
            final_result = result

            if result.get("status") == "ACCEPT" and getattr(step, "conclusion", None):
                kb.add_fact(step.conclusion, source="inference")

            if result.get("status") == "REJECT":
                failure = self.failure_detector.detect(step, result)
                repair = self.repair_engine.suggest(failure) if failure else None
                return {
                    "status": result.get("status"),
                    "rule": result.get("rule"),
                    "steps_evaluated": steps_evaluated,
                    "failure": failure,
                    "repair": repair,
                    "reasoning_trace": self.trace_graph.get_trace(),
                }

        return {
            "status": final_result.get("status") if final_result else "SUSPEND",
            "rule": final_result.get("rule") if final_result else None,
            "steps_evaluated": steps_evaluated,
            "failure": None,
            "repair": None,
            "reasoning_trace": self.trace_graph.get_trace(),
        }
