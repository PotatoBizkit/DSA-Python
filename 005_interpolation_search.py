def interpolationSearch(val):
    lo = 0
    hi = MAX - 1
    mid = -1
    index = -1
    comparisons = 1
    while (lo < hi and val >= num[lo] and val <= num[hi] and num[hi] != num[lo]):
        print(f"Comparisons {comparisons}")
        print(f"low = {lo} and num[{lo}] = {num[lo]}")
        print("high = {} and num[{}] = {}".format(hi, hi, num[hi]))
        comparisons += 1
        
        mid = int(lo + ((hi - lo)*((val - num[lo])/(num[hi] - num[lo]))))
        print(f"mid = {mid}")

        if (num[mid] == val):
            index = mid
            break
        elif (num[mid] < val):
            lo = mid + 1
        elif (num[mid] > val):
            hi = mid - 1
        
    print(f"Total comparisons = {comparisons-1}")
    return index

if __name__ == '__main__':
    MAX = 10
    num = [10, 14, 19, 26, 27, 31, 33, 35, 42, 44]
    ind = interpolationSearch(33)
    if (ind != -1):
        print(f"Element found at index {ind}")
    else:
        print("Element not found")