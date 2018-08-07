def fib(n):
    left = 0
    right = 1
    num = n*[0]
    for i in range(1,n):
        next = left + right
        left = right
        right = next
        num[i] = right
    print(num)
    return right


print(fib(9))
print(fib(10))
