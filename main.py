from analysis import classify, describe

stocks = [
    {"ticker": "AAPL", "pe": 28},
    {"ticker": "F", "pe": 7},
    {"ticker": "KO", "pe": 24},
]

for stock in stocks:
    stock["label"] = classify(stock["pe"])
    print(describe(stock))