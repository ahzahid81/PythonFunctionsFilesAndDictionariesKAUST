travel = {"North America": 2, "Europe": 8, "South America": 3, "Asia": 4, "Africa":1, "Antarctica": 0, "Australia": 1}

total = 0

for continent in travel:
    total = total + travel[continent]
    
print(total)