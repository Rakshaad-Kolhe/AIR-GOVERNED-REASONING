class DatasetBuilder:
    def __init__(self):
        self.samples = []

    def add(self, sample):
        if sample:
            self.samples.append(sample)

    def build(self):
        dataset = []

        for sample in self.samples:
            dataset.append(
                {
                    "question": sample["question"],
                    "failure_type": sample["failure_type"],
                    "repair_suggestion": sample["repair_suggestion"],
                    "trace": sample["trace"],
                }
            )

        return dataset
