num = None

# YOUR CODE HERE
with open("assets/travel_plans.txt","r") as f:
    num = len(f.read())

assert num == 316