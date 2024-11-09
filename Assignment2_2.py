s1 = 'hello'
counts = None
counts = {}

for letter in s1:
    if letter not in counts:
        counts[letter] = 0
    counts[letter] += 1
    
print(counts)