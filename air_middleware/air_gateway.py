class AIRGateway:
    def __init__(self, reasoning_loop, trace_store):
        self.reasoning_loop = reasoning_loop
        self.trace_store = trace_store

    def reason(self, question, kb):
        result = self.reasoning_loop.run(question, kb)
        self.trace_store.save_trace(question, result)
        return result
