three = None

three = []

with open("assets/school_prompt.txt", "r") as f:
    for line in f:
        words = line.split()
        
        if len(words)>3:
            three.append(words[2])
            
assert type(three) == list
assert len(three) == 10