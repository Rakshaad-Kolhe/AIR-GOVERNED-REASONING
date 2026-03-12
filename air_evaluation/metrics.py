class AIRMetrics:
    def __init__(self):
        self.total = 0
        self.accepted = 0
        self.rejected = 0

    def record(self, result):
        self.total += 1

        status = result.get("status")

        if status == "ACCEPT":
            self.accepted += 1

        if status == "REJECT":
            self.rejected += 1

    def summary(self):
        return {
            "total": self.total,
            "accepted": self.accepted,
            "rejected": self.rejected,
        }