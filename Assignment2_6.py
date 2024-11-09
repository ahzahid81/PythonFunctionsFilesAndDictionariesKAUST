sally = 'sally sells sea shells by the sea shore and by the road'
characters = None
worst_char = None

characters = {}

for char in sally:
    if char not in characters:
        characters[char] = 0
        
    characters[char] +=1
    
key = list(characters.keys())
worst_char = key[0]

for best in characters:
    if characters[best] < characters[worst_char]:
        worst_char = best
        
print(characters)
print(worst_char)
