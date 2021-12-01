import sys
from functools import reduce

class Bag:
    def __init__(self, desc):
        attributes = desc.split(" ")
        attributes.pop()
        if len(attributes) == 3:
            self.amount = attributes.pop(0)
        self.tone, self.color = tuple(attributes)

    def toTuple(self, withAmount = False):
        if withAmount:
            return self.amount, self.tone, self.color
        else:
            return self.tone, self.color


inside2outside = {}
outside2inside = {}

def lookupContainers(query, sofar={}):
    if query not in inside2outside:
        return {}
    containers = inside2outside[query]
    for container in containers:
        sofar[container] = True
        lookupContainers(container, sofar)
    return sofar

def sumContents(query):
    if query not in outside2inside:
        return 0
    contents = outside2inside[query]
    total = 0
    for amount, tone, color in contents:
        partial = int(amount) * (sumContents((tone, color)) + 1)
        print("%s contains %s and therefore %d are added" % (query, (amount, tone, color), partial))

        total += partial
    return total

for line in sys.stdin.readlines():
    line = line.strip()
    container, contents = line.split(" contain ")
    contents = contents.rstrip(".")
    if contents != "no other bags":
        containerBag = Bag(container)
        for content in contents.split(", "):
            contentBag = Bag(content)
            inside2outside.setdefault(contentBag.toTuple(), []).append(containerBag.toTuple())
            outside2inside.setdefault(containerBag.toTuple(), []).append(contentBag.toTuple(True))

print(outside2inside)

query = "shiny", "gold"

posibleContainers = lookupContainers(query)
print(len(posibleContainers))
totalContents = sumContents(query)
print(totalContents)