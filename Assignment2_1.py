str1 = 'peter piper picked a peck of pickled peppers'
freq = None
freq = {}

for char in str1:
    if char not in freq:
        freq[char] = 0
    freq[char] += 1
    

print(freq)