class Queue:
    def __init__(self):
        self.queue = []
        self.front = -1
        self.rear = -1
        self.MAX = 5
    
    def isEmpty(self):
        return self.front == -1 or self.front > self.rear
    
    def isFull(self):
        return self.rear == self.MAX - 1
    
    def enqueue(self, value):
        if not self.isFull():
            if self.isEmpty():
                self.front = 0
            self.rear += 1
            self.queue.append(value)
        else:
            print("Queue Full")

    def dequeue(self):
        if not self.isEmpty():
            data = self.queue.pop(self.front)
            self.front += 1
            return data
        else:
            print("Queue Empty")
    
    def display(self):
        if not self.isEmpty():
            for x in self.queue:
                print(x, end=" ")
            print()
        else:
            print("Empty Queue")
    
    def peek(self):
        print(f"Front: {self.queue[0]}")
        print(f"Rear: {self.queue[-1]}")

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)

q.display()

print(q.dequeue())
q.display()
q.peek()