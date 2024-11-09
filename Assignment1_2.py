num_words = None
# YOUR CODE HERE
with open("assets/emotion_words.txt","r") as f:
    words = f.read().split()
    
num_words = len(words)

assert num_words == 48