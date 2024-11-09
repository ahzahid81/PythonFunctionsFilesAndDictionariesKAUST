inventory = {'apples': 430, 'bananas': 312, 'pears':217, 'orange':525}

for akey in inventory.keys():
    print("Got key", akey, "which maps to value", inventory[akey])
    
ks = list(inventory.keys())
print(ks)
print(ks[0])