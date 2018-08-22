import itertools

def check(num):
    r = [perm for perm in itertools.permutations(num)]
    max = 0
    for item in r:
        hour = str(item[0])+str(item[1])
        time = str(item[2])+str(item[3])
        if(int(hour)<=24 and int(time) <= 60):
            result = int(hour)*100+int(time)
            if result > max:
                max = result
    return max

print(check([1,2,3,4]))
print(check([5,3,2,1]))
