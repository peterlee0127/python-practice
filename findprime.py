for nu in range(1,100):
    prime = True
    for n in range(2,nu-1):
        if nu % n == 0:
            prime = False
    if prime == True:
        print(nu)
