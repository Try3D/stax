from sys import argv
from stack import Stack

if len(argv) != 2:
    print("Usage: stack [file].stk")
    exit(1)

try:
    with open(argv[1]) as f:
        lines = f.readlines()
except FileNotFoundError:
    print("File not found")
    exit()

stacks = {}
current_stack = None

for line in lines:
    tokens = line.strip().split()

    if len(tokens) == 1 and tokens[0].endswith(';'):
        stack_name = tokens[0][:-1]
        stacks[stack_name] = Stack()
        current_stack = stack_name

    else:
        command = tokens[0]
        if command == "PUSH":
            value = int(tokens[1])
            stack_name = tokens[2][:-1]
            stacks[stack_name].push(value)
        elif command == "PRINT":
            stack_name = tokens[1][:-1]
            stacks[stack_name].print()
        elif command == "ADD":
            stack_name = tokens[1][:-1]
            stacks[stack_name].add()
