class ConstraintStats:
    def __init__(self, constraint_library):
        self.constraint_library = constraint_library

    def summary(self):
        stats = self.constraint_library.get_statistics()
        total = sum(stats.values())
        summary = {}

        for key, count in stats.items():
            percent = (count / total * 100) if total else 0.0
            summary[key] = {"count": count, "percent": round(percent, 1)}

        return summary

    def print_report(self):
        summary = self.summary()

        print("AIR Constraint Analytics")
        print("")

        if not summary:
            print("No constraints learned yet.")
            return

        width = max(len(name) for name in summary.keys())
        for name, data in summary.items():
            print(f"{name.ljust(width)} : {data['percent']}%")
