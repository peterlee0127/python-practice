
def twosum(num,ans):
    print(num)
    print(ans)
    dict = {}
    for nu in num:
        if nu in dict:
            print(str(dict[nu])+" "+str(nu))
        else:
            dict[ans-nu] = nu



twosum([1,2,3,6,10,15,16,17],18)
twosum([1,2,3,2,10,15,16,17],17)
