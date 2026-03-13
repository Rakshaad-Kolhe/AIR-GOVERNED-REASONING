from governance.eal_engine import EALEngine
from air_runtime.failure_detector import FailureDetector
from air_runtime.repair_engine import RepairEngine
from air_trace.trace_graph import TraceGraph

# NEW IMPORTS
from air_constraints.constraint_library import ConstraintLibrary
from air_constraints.constraint_extractor import ConstraintExtractor
from air_constraints.constraint_generalizer import ConstraintGeneralizer


class AIRExecutor:
    def __init__(self):
        self.engine = EALEngine()
        self.failure_detector = FailureDetector()
        self.repair_engine = RepairEngine()
        self.trace_graph = TraceGraph()

        # NEW COMPONENTS
        self.constraint_library = ConstraintLibrary()
        self.constraint_extractor = ConstraintExtractor()
        self.constraint_generalizer = ConstraintGeneralizer()

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
            constraints = self.constraint_library.match(step.premises)
            if constraints:
                self.trace_graph.add_constraint(constraints)
                result = {
                    "status": "REJECT",
                    "rule": step.operator,
                    "constraint_triggered": True,
                    "constraints": constraints,
                }
                self.trace_graph.add_step(step, result)

                steps_evaluated += 1

                return {
                    "status": "REJECT",
                    "rule": step.operator,
                    "steps_evaluated": steps_evaluated,
                    "failure": {"error_type": "constraint_violation"},
                    "repair": None,
                    "reasoning_trace": self.trace_graph.get_trace(),
                }
                
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

                # NEW: extract constraint from failure
                constraint = self.constraint_extractor.extract(step, failure)

                if constraint:
                    generalized_constraint = self.constraint_generalizer.generalize(constraint)

                    if generalized_constraint:
                        self.constraint_library.add(generalized_constraint)

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
