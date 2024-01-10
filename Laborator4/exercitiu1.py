# Write a Python class that simulates a Stack.
# The class should implement methods like push, pop, peek
# (the last two methods should return None if no element is present in the stack).

class Stack:
    def __init__(self):
        self.top = 0
        self.my_stack = []
        self.is_empty = True

    def push(self, value):
        self.my_stack.append(value)
        self.is_empty = False
        self.top += 1

    def pop(self):
        if self.is_empty:
            print(" Stack is empty, there is nothing to pop")
            return None
        else:
            popped_element = self.my_stack.pop()
            self.top -= 1
            if self.top == 0:
                self.is_empty = True
            return popped_element

    def peek(self, ):
        if self.is_empty:
            print(" The Stack is empty, there is no element to peek :(")
            return None
        else:
            peek_element = self.my_stack.pop()
            self.my_stack.append(peek_element)
            return peek_element


stack = Stack()
stack.push(4)
stack.push(5)
stack.push(1)
stack.push(10)
stack.pop()
a = stack.peek()
another_stack = Stack()
print(stack.my_stack, a, another_stack.my_stack)
