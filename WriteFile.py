filename = 'C:\\Users\\btozier\\Desktop\\Remote Type Test.txt'

target = open(filename, 'w')

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

target.close()