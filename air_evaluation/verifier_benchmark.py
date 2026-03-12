class VerifierBenchmark:
    def __init__(self, supervisor, kb, metrics):
        self.supervisor = supervisor
        self.kb = kb
        self.metrics = metrics

    def run(self, questions):
        for question in questions:
            result = self.supervisor.run(question, self.kb)
            self.metrics.record(result)

        return self.metrics.summary()
