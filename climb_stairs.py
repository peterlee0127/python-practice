# climb stairs
# compute all posibility of climb. each time only 1 or 2 steps.
#  
#
# top-down
#  f(0) = 1 and f(1) = 1
#  f(n) = f(n-1) + f(n-2)
#
num = 5
table = [0] * (num+1)

def climb(n):
    if n == 0 or n == 1:
        table[n] = 1
        return table[n]
    if table[n] != 0:
        return table[n]    
    table[n] = climb(n-1)+ climb(n-2)
    return table[n]

ans = climb(num)
print(table[1:])

#
### bottom-up
#
# [1,1,0,0,0,0]
table = [1,1] 
for i in range(0,num-1):
    table.append(0)
    
for i in range(2,num+1):
    table[i] = table[i-1] + table[i-2]
print(table[1:])

