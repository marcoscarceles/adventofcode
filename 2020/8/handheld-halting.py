import sys

operations = []
counter = 0
stack = []

def execute(statement):
    global counter
    if statement in stack:
        return
    stack.append(statement)
    operation = operations[statement][0]
    argument = int(operations[statement][1])
    if operation == "nop":
        statement += 1
    elif operation == "acc":
        counter += argument
        statement += 1
    elif operation == "jmp":
        statement += argument
    execute(statement)    

for line in sys.stdin.readlines():
    line = line.strip()
    operations.append(line.split(" "))

execute(0)
print(counter)

