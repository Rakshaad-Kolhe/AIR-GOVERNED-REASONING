class TraceStore:
    def __init__(self):
        self.traces = []

    def save_trace(self, question, result):
        trace_record = {
            "question": question,
            "status": result.get("status") if isinstance(result, dict) else None,
            "failure": result.get("failure") if isinstance(result, dict) else None,
            "reasoning_trace": result.get("reasoning_trace") if isinstance(result, dict) else None,
        }
        self.traces.append(trace_record)

    def get_all_traces(self):
        return self.traces

    def export_dataset(self):
        dataset = []
        for trace in self.traces:
            dataset.append(
                {
                    "input_question": trace.get("question"),
                    "reasoning_trace": trace.get("reasoning_trace"),
                    "status": trace.get("status"),
                    "failure": trace.get("failure"),
                }
            )
        return dataset
