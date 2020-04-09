
file = open('Text.txt')
#file.read(5)
#print(file.readline())

# Read all lines of a file using readline method
#Method 1
line = file.readline()
while line!="":
    print(line)
    line=file.readline()

#Method 2 (Using readlines)

for line in file.readlines():
    print(line)
file.close()

