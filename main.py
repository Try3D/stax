from sys import argv


class Stack:
    def __init__(self) -> None:
        self.stack = []

    def push(self, n: int) -> None:
        self.stack += [n]

    def pop(self) -> int:
        return self.stack.pop()

    def print(self) -> None:
        print(self.stack[-1])

    def add(self) -> int:
        a = self.pop()
        b = self.pop()
        c = a + b

        self.push(c)
        return c

    def subtract(self) -> int:
        a = self.pop()
        b = self.pop()
        c = a - b

        self.push(c)
        return c

    def multiply(self) -> int:
        a = self.pop()
        b = self.pop()
        c = a * b

        self.push(c)
        return c

    def divide(self) -> int:
        a = self.pop()
        b = self.pop()
        c = a // b

        self.push(c)
        return c

    def mod(self) -> int:
        a = self.pop()
        b = self.pop()
        c = a % b

        self.push(c)
        return c


def main():
    if len(argv) > 2:
        print("Usage: stack [file].stax")
        exit()

    stacks = {}

    if len(argv) == 1:
        print(f"Stax interactive shell v(0.0.1)")
        while True:
            print(">>> ", end="")
            line = input()
            execute_commands(line, stacks)

    try:
        with open(argv[1]) as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("File not found")
        exit()

    for line in lines:
        execute_commands(line, stacks)


def execute_commands(line, stacks):
    line = line.strip()

    if not line:
        return

    tokens = line.split()

    if len(tokens) == 1 and tokens[0].rstrip(";") == "EXIT":
        exit()

    elif len(tokens) == 1 and tokens[0].endswith(";"):
        stack_name = tokens[0][:-1]
        stacks[stack_name] = Stack()

    else:
        command = tokens[0]
        if command == "PUSH":
            try:
                value = eval(" ".join(tokens[1:-1]))
            except NameError:
                value = " ".join(tokens[1:-1])
            stack_name = tokens[-1][:-1]
            stacks[stack_name].push(value)
        elif command == "POP":
            stack_name = tokens[-1][:-1]
            stacks[stack_name].pop()
        elif command == "PRINT":
            stack_name = tokens[-1][:-1]
            stacks[stack_name].print()
        elif command == "ADD":
            stack_name = tokens[-1][:-1]
            stacks[stack_name].add()
        elif command == "SUBT":
            stack_name = tokens[-1][:-1]
            stacks[stack_name].subtract()
        elif command == "MULT":
            stack_name = tokens[-1][:-1]
            stacks[stack_name].multiply()
        elif command == "DIV":
            stack_name = tokens[-1][:-1]
            stacks[stack_name].divide()
        elif command == "MOD":
            stack_name = tokens[-1][:-1]
            stacks[stack_name].mod()


if __name__ == "__main__":
    main()
