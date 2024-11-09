f = open('scarlet.txt','r')
txt = f.read()

t_count = 0
for c in txt:
    if c == 't':
        t_count = t_count + 1

print("t: " +str(t_count) + " occurrences")