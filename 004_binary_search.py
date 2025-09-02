def binarySearch(arr, low, high, key):
    mid = (low + high)//2
    if low <= high:
        if arr[mid] == key:
            print(f"Element found at index {mid}")
        elif arr[mid] > key:
            binarySearch(arr, low, mid-1, key)
        elif arr[mid] < key:
            binarySearch(arr, mid+1, high, key)
    else:
        print("Unsuccessful search")

l = [1,2,3,4,5,6,7,8,9,10]
low = 0
high = len(l) - 1
key = 11
binarySearch(l, low, high, key)