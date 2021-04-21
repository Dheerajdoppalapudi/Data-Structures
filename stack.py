class Stack:
    def __init__(self, limit):
        self.stack = []
        self.count = -1
        self.limit = limit

    def push(self, data):
        if self.count == self.limit-1:
            print("Stack is Full")
        else:
            self.stack.append(data)
            self.count += 1

    def pop(self):
        if self.count == -1:
            print("nothing to pop, stack is Empty")
        else:
            ele = self.stack[-1]
            self.stack = self.stack[:-1]
            print("popped: ", ele)
            self.count -= 1

    def peek(self):
        if self.count == -1:
            print("Stack is Empty")
        else:
            print("Top element of the stack is: ", self.stack[self.count])

    def isEmpty(self):
        if self.count == -1:
            print("Stack is Empty")
        else:
            print("Stack is Not Empty")

    def isFull(self):
        if self.count == self.limit-1:
            print("Stack is Full")
        else:
            print("Stack is Not Full")

    def showStack(self):
        print("Stack: ", self.stack)

limit = int(input("Enter the size of Stack: "))
object = Stack(limit)
while True:
    print("------------------------------------------------")
    print("1 -> print stack")
    print("2 -> push")
    print("3 -> pop")
    print("4 -> check if stack is full or not")
    print("5 -> check if stack is Empty")
    print("6 -> peek")
    print("ENTER any key to terminate program")
    n = int(input("enter an option: "))
    if n == 1:
        object.showStack()
    elif n == 2:
        data = int(input("enter the Data: "))
        object.push(data)
    elif n == 3:
        object.pop()
    elif n == 4:
        object.isFull()
    elif n == 5:
        object.isEmpty()
    elif n == 6:
        object.peek()
    else:
        print("Program Terminated")
        break