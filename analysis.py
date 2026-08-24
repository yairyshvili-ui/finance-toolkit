def classify(pe):
    if pe < 15:
        return "Cheap"
    elif pe < 25:
        return "Fair"
    else:
        return "Expensive"


def describe(stock):
    return stock["ticker"] + ": " + stock["label"]