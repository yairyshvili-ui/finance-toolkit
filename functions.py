def classify(pe):
    if pe < 15:
        return "Cheap"
    elif pe < 25:
        return "Fair"
    else:
        return "Expensive"
    
print(classify(12))
print(classify(30))
print(classify(8))
print(classify(20))
print(classify(50))
print(classify(14))