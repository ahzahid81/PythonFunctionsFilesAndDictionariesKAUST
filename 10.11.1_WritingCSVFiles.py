n = [0]*12

for i in range(1,13):
    n[i-1] = i*12
outfile = open("Multiples of 12", "w")

for j in range(0, len(n)):
    outfile.write(str(j+1) + ',' + str(n[j]))
    outfile.write('\n')
    
outfile.close()
