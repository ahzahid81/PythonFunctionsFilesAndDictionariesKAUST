### Create the dictionary characters that shows 
# each character from the string sally and its 
# frequency. Then, find the most frequent letter 
# based on the dictionary. Assign this letter to 
# the variable best_char.

sally = 'sally sells sea shells by the sea shore'
characters = None
best_char = None

characters = {}

for char in sally:
    if char not in characters:
        characters[char] = 0
        
    characters[char] +=1
    
key = list(characters.keys())
best_char = key[0]

for best in characters:
    if characters[best] > characters[best_char]:
        best_char = best

# YOUR CODE HERE
raise NotImplementedError()