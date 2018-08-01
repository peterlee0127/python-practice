def removeDuplicates(nums):
    dict = {}
    arr = []
    for item in nums:
        if dict[item] != 1:
            dict[item] = 1
            arr.append(item)
    return arr

arr = [1,3,4,5,4,2,2,2,74,23]
arr = removeDuplicates(arr)
print(arr)
