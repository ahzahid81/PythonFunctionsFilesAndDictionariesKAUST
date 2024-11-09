beginning_chars = None

# YOUR CODE HERE
with open("assets/school_prompt.txt","r") as f:
    beginning_chars = f.read()[:30]
print(beginning_chars)

assert type(beginning_chars) == str
assert len(beginning_chars) == 30