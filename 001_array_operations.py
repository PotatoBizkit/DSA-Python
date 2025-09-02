def insertion(array):
    print("Array before any insertions:")
    for i, val in enumerate(array):
        print(f"arr[{i}] = {val}")
    for i in range(len(array)):
        array[i] = int(input(f"Insert Element {i + 1}\n"))
    print("Array after insertions:")
    for i, val in enumerate(array):
        print(f"arr[{i}] = {val}")

def deletion(array):
    print("Original Array:")
    for i, val in enumerate(array):
        print(f"arr[{i}] = {val}")
    for i in range(len(array) - 1):
        array[i] = array[i + 1]
    array.pop()
    print("Array after deletion:")
    for i, val in enumerate(array):
        print(f"arr[{i}] = {val}")

def display(array):
    print("Displaying array:")
    for i, val in enumerate(array):
        print(f"arr[{i}] = {val}")

def update(array):
    try:
        n = int(input("Enter the element no. you want to change:\n"))
        array[n-1] = int(input("Enter the value:\n"))
        display(array)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    arr = [0] * 5
    arrd = [1,2,3,4,5]
    # insertion(arr)
    # deletion(arrd)
    # display(arrd)
    update(arrd)
    print()