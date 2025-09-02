class DynamicStack:
    def __init__(self):
        self.stack = []
        self.top = -1
        self.MAX = 100
    
    def isEmpty(self):
        return self.top == -1
    
    def isFull(self):
        return self.top == self.MAX - 1
    
    def push(self, value):
        if not self.isFull():
            self.stack.append(value)
            self.top += 1
        else:
            print("Overflow")
    
    def pop(self):
        if not self.isEmpty():
            data = self.stack.pop()
            self.top -= 1
            return data
        else:
            print("Underflow")
    
    def display(self):
        for x in self.stack:
            print(x, end=" ")
        print()
        
    def peek(self):
        if not self.isEmpty():
            print(self.stack[self.top])

s = DynamicStack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)

s.display()

print(s.pop())

s.display()
s.peek()