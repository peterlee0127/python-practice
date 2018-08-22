import itertools

def check(num):
    r = [perm for perm in itertools.permutations(num)]
    max = 0
    for item in r:
        hour = item[0]*10+item[1]
        time = item[2]*10+item[3]
        if(hour<=24 and time <= 60):
            result = hour*100+time
            if result > max:
                max = result
    return max

print(check([1,2,3,4]))
print(check([5,3,2,1]))
print(check([5,3,4,6]))
