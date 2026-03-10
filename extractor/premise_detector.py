class PremiseDetector:
    def extract(self, text):
        premises = []
        for line in str(text).splitlines():
            stripped = line.strip()
            if stripped.startswith("Premise:"):
                premise = stripped[len("Premise:"):].strip()
                premises.append(premise)
        return premises
