""" Stack Implementation """
class Stack:
    def __init__(self):
        self.stack = []
    def push(self, data):
        self.stack.append(data)
    def pop(self) -> None:
        # pop the toppest value in stack
        self.stack.pop()
    def peek(self):
        return self.stack[-1]
    def print_all(self):
        return self.stack

if __name__ == "__main__":
    stack = Stack()
    stack.push(123)
    stack.push(456)
    print(stack.print_all())
    print(stack.peek())
    stack.pop()
    print(stack.print_all())