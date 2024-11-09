num_lines = None

# YOUR CODE HERE
with open("assets/school_prompt.txt","r") as f:
    line = f.readlines()
    
num_lines = len(line)

assert num_lines == 10