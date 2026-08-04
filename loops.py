pe_ratios = [12, 20, 30, 8, 25]

for pe in pe_ratios:
    if pe < 15:
        print(pe, "Cheap")
    elif pe < 25:
        print(pe, "Fair")
    else:
        print(pe, "Expensive")
        