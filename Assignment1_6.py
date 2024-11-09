emotions = None
emotions = []

with open("assets/emotion_words.txt", "r") as f:
    for lines in f:
        word = lines.split()
        
        if len(word)>2:
            emotions.append(word[0])

assert type(emotions) == list
assert len(emotions) == 7