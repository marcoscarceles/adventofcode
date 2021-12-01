import sys

anySum = 0
count = dict()
everySum = 0
groupSize = 0

for line in sys.stdin.readlines():
    line = line.strip()
    if line:
        groupSize += 1
        for answer in line:
           count[answer] = count.get(answer, 0) + 1
    else:
        anySum += len(count)
        for answers in count.values():
            everySum += 1 if answers == groupSize else 0
        count = dict()
        groupSize = 0
        
if count:
    anySum += len(count)
    for answers in count.values():
        everySum += 1 if answers == groupSize else 0

print(anySum)
print(everySum)

