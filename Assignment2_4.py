sent = 'Singing in the rain and playing in the rain are two entirely different situations but both can be good'
wrd_d = None
wrd_d = {}

for word in sent.split():
    if word not in wrd_d:
        wrd_d[word] = 0
    wrd_d[word] += 1
# YOUR CODE HERE
print(wrd_d)