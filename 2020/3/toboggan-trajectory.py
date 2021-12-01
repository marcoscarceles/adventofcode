import sys

if len(sys.argv) != 2:
    sys.exit("Expected input file.")

fileName = sys.argv[1]


with open(fileName, 'r') as file: 
    forest = [line.strip() for line in file]

height = len(forest)
width = len(forest[0])
print("Forest is %dw x %dl" % (width, height))

slopes = (1,1), (3,1), (5,1), (7,1), (1, 2)
trees = []

output = 1

for right, down in slopes:
    count = 0
    offset = 0
    for step in range(0, height, down):
        if(forest[step][offset] == '#'):
            count += 1
        offset = (offset + right) % width
    result = right, down, count
    print("Moving %d right %d down you'd hit exactly %d trees" % result)
    trees.append(result)
    output *= count

print("Output is %d" % output)

