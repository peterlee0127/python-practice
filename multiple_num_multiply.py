#
# This problem was asked by Uber.
#
# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
#
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
#
# Follow-up: what if you can't use division?


def multiple_num_multiply(num):
    right = [1] * len(num)
    left = [1] * len(num)
    ans = [1] * len(num)
    for index in range(1, len(num)):
        left[index] = left[index-1] * num[index-1]

    for index in range(len(num)-2, -1, -1):
        right[index] = right[index+1] * num[index+1]

    for index in range(0, len(num)):
        ans[index] = left[index] * right[index]

    #print(left)
    #print(right)
    print(ans)
    return ans

multiple_num_multiply([2, 3, 1, 4, 5])
multiple_num_multiply([3,1,10,2])
