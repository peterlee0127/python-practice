# n! = 4.3.2.1
n = 5
a = [0,1]

for i in range(2,n+1):
    a.append(a[i-1]*i)

print(a)
