s = "school_prompt2.txt"
with open(s, "r") as f:
    print(f.read(10))
    lines = f.readlines()
    for line in lines:
        print(line[0])
    for line in lines:
        print(line[-1])
        
    