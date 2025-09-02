def linearSearch(array, value):
    # found = 0
    # for i in range(len(array)):
    #     if array[i] == value:
    #         print("Value present")
    #         found = 1
    # if found == 0:
    #     print("Value not present")
    if value in array:
        print("Value present")
    else:
        print("Value not present")

arr = [1,2,3,4,5]
value = int(input("Enter the value you want to search:\n"))
linearSearch(arr, value)