inventory = {'apples':430, 'bananas':312, 'oranges':525, 'pears':217}

print(list(inventory.items()))

for k,v in inventory.items():
    print("Got", k, "that maps to", v)