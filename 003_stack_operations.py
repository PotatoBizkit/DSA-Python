MAXSIZE = 8
stack = []
top = -1

def isEmpty():
    return top == -1

def isFull():
    return len(stack) == MAXSIZE

def push(data):
    global top
    if not isFull():
        stack.append(data)
        top += 1
    else:
        print("Overflow")

def pop():
    global top
    if not isEmpty():
        data = stack.pop()
        top -= 1
        return data
    else:
        print("Underflow")