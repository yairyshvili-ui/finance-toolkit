def classify(pe):
    if pe < 15:
        return "Cheap"
    elif pe < 25:
        return "Fair"
    else:
        return "Expensive"

stocks = [
    {"ticker": "AAPL", "pe": 28},
    {"ticker": "F", "pe": 7},
    {"ticker": "KO", "pe": 24},
]

for stock in stocks:
    stock["label"] = classify(stock["pe"])

print(stocks)



