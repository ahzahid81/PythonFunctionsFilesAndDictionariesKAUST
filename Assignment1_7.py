first_chars = None

# YOUR CODE HERE
with open("assets/travel_plans.txt", "r") as f:
    first_chars = f.read(33)
    
assert type(first_chars) == str
assert len(first_chars) == 33