p_words = None
p_words = []
with open("assets/school_prompt.txt", "r") as f:
    words = f.read().split()
    
    for word in words:
        if "p" in word:
            p_words.append(word)

assert type(p_words) == list
assert len(p_words) == 5