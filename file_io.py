import json

def classify(pe):
    if pe < 15:
        return "Cheap"
    elif pe < 25:
        return "Fair"
    else:
        return "Expensive"

with open("stocks.json") as f:
    stocks = json.load(f)

for stock in stocks:
    stock["label"] = classify(stock["pe"])

with open("report.json", "w") as f:
    json.dump(stocks, f, indent=4)

print("Report saved to report.json")