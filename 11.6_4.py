f = open('scarlet.txt', 'r')

txt = f.read()

letter_counts = {}
letter_counts['t'] = 0
letter_counts['s'] = 0

for c in txt:
    if c == 't':
        letter_counts[c] = letter_counts[c] + 1
    elif c == 's':
        letter_counts[c] = letter_counts[c] + 1
        


print("t: " +str(letter_counts['t']) + " occurrences")
print("s: " +str(letter_counts['s'])+ " occurrences")