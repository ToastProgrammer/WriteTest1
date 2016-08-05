filename = 'C:\\Users\\btozier\\Desktop\\Remote Type Test.txt'

target = open(filename, 'w')

line1 = "Did"
line2 = "It"
line3 = "Work?"

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

target.close()
