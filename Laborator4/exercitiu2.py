# Write a Python class that simulates a Queue.
# The class should implement methods like push, pop, peek
# (the last two methods should return None if no element is present in the queue).
import copy


class Queue:
    def __init__(self):
        self.top = 0
        self.my_queue = []
        self.is_empty = True

    def push(self, value):
        self.my_queue.append(value)
        self.is_empty = False
        self.top += 1

    def pop(self):
        if self.is_empty:
            print(" Stack is empty, there is nothing to pop")
            return None
        else:
            popped_element = self.my_queue.pop(0)
            self.top -= 1
            if self.top == 0:
                self.is_empty = True
            return popped_element

    def peek(self, ):
        if self.is_empty:
            print(" The Stack is empty, there is no element to peek :(")
            return None
        else:
            lista_copie = copy.deepcopy(self.my_queue)
            peek_element = self.my_queue.pop(0)
            self.my_queue = lista_copie
            return peek_element




queue = Queue()
queue.push(10)
queue.push(4)
queue.push(5)
queue.push(1)
queue.push(21)
queue.pop()
a = queue.peek()
print(queue.my_queue, a)
