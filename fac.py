# n! = 4.3.2.1

a = []
a.append(0)
a.append(1)
n = 100+2
print(a)

for i in range(2,n):
    a.append(a[i-1]*i)

print(a)
