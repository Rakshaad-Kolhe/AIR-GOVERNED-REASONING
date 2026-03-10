class Metrics:
    def __init__(self):
        self.reset()

    def record(self, result):
        status = None
        if isinstance(result, dict):
            status = result.get("status")
        else:
            status = result

        if status in self.counters:
            self.counters[status] += 1

    def summary(self):
        return {
            "ACCEPT": self.counters["ACCEPT"],
            "REJECT": self.counters["REJECT"],
            "SUSPEND": self.counters["SUSPEND"],
        }

    def reset(self):
        self.counters = {
            "ACCEPT": 0,
            "REJECT": 0,
            "SUSPEND": 0,
        }
