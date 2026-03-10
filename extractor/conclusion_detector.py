class ConclusionDetector:
    def extract(self, text):
        conclusions = []
        for line in str(text).splitlines():
            stripped = line.strip()
            if stripped.startswith("Conclusion:"):
                conclusion = stripped[len("Conclusion:"):].strip()
                conclusions.append(conclusion)
        return conclusions
