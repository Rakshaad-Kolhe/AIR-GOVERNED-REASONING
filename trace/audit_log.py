from datetime import datetime


class AuditLog:
    def __init__(self):
        self.entries = []

    def record(self, result):
        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "status": result.get("status"),
            "rule": result.get("rule"),
            "trace": list(result.get("trace", [])),
        }
        self.entries.append(entry)

    def get_logs(self):
        return list(self.entries)

    def clear(self):
        self.entries = []
