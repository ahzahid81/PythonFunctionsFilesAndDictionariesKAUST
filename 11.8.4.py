product = "iphone and android phones"

lett_d = {}

for char in product:
    if char not in lett_d:
        lett_d[char] = 0
    lett_d[char] = lett_d[char] + 1
    
list = list(lett_d.keys())
key = list[0]

for max in list:
    if lett_d[max] > lett_d[key]:
        key = max
        
key_with_max_value = lett_d[key]
print(key_with_max_value)
