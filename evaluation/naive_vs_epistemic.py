from governance.eal_engine import EALEngine


def naive_inference(rules):
    return "ACCEPT" if rules else "SUSPEND"


def epistemic_inference(kb, rules):
    engine = EALEngine()
    return engine.evaluate(kb, rules)


def compare(kb, rules):
    return {
        "naive": naive_inference(rules),
        "epistemic": epistemic_inference(kb, rules),
    }
