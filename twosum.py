num = [1,2,3,6,10,15,16,17]
ans = 18
answer = []


def twosum(num,ans):
    dict = {}
    for nu in num:
        if nu in dict:
            answer.append([dict[nu], nu])
        else:
            dict[ans-nu] = nu



out = twosum(num,ans)
print(answer)
