placement = "Beaches are cool places to visit in spring however the Mackinaw Bridge is near. Most people visit Mackinaw later since the island is a cool place to explore."
d = {}

for char in placement:
    if char not in d:
        d[char] = 0
    
    d[char] = d[char] + 1
    
keys = list(d.keys())

key_with_min_value = 'a'

for min in keys:
    if d[min] < d[key_with_min_value]:
        key_with_min_value = min

print(d.keys())
print(d.values())
print( key_with_min_value)