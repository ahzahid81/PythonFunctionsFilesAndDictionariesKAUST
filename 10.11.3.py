olympians = [("John Aalberg", 31, "Cross Country Skiing"), ("Minna Maarit Aalto", 30, "Sailing"), ("Win Valdemer Aaltonen", 54, "Art Competitions"),
("Wakako Abe", 18, "Cycling")]

outfile = open('reduced_olympics2.csv', "w")

outfile.write('"Name", "Age", "Sport"')
outfile.write('\n')

for olympian in olympians:
    row_string = '{},{},{}'.format(olympian[0], olympian[1], olympian[2])
    outfile.write(row_string)
    outfile.write('\n')

outfile.close()
    