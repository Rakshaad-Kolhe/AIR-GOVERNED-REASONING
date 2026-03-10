from evaluation.metrics import Metrics
from governance.eal_engine import EALEngine


class BenchmarkRunner:
    def __init__(self):
        self.engine = EALEngine()
        self.metrics = Metrics()

    def run(self, kb, rules_list):
        for rules in rules_list:
            result = self.engine.evaluate(kb, rules)
            self.metrics.record(result)

    def results(self):
        return self.metrics.summary()
