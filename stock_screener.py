def classify(pe):
    if pe < 15:
        return "Cheap"
    elif pe < 25:
        return "Fair"
    else:
        return "Expensive"

stocks = [
    {"ticker": "AAPL", "price": 227.5, "pe": 28},
    {"ticker": "MSFT", "price": 415.0, "pe": 35},
    {"ticker": "F", "price": 11.2, "pe": 7},
    {"ticker": "KO", "price": 62.0, "pe": 24},
]

for stock in stocks:
    label = classify(stock["pe"])
    print(stock["ticker"], stock["pe"], label)
    cheap_count = 0
fair_count = 0
expensive_count = 0

for stock in stocks:
    label = classify(stock["pe"])
    if label == "Cheap":
        cheap_count = cheap_count + 1
    elif label == "Fair":
        fair_count = fair_count + 1
    else:
        expensive_count = expensive_count + 1

print("---")
print("Cheap:", cheap_count)
print("Fair:", fair_count)
print("Expensive:", expensive_count)