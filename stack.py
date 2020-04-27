class Stack:

    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return self.stack == []
        # if len(self.stack) == 0:
        #     return True
        # else:
        #     return False

    def push(self,data):
        self.stack.append(data)

    def peek(self):
        return self.stack[-1]

    def pop(self):
        data = self.stack[-1]
        del self.stack[-1]
        return data    

    def sizeStack(self):

        return len(self.stack)

    def printStack(self):

        return self.stack

stack = Stack()
print("isEmpty",stack.isEmpty())
stack.push(3)
stack.push(4)
stack.push(34)
stack.push(94)
print("stack:", stack.printStack())
stack.pop()
print("stack:", stack.printStack())