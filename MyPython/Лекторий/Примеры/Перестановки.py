def find(n, pr):
    for i in pr:
        if i == n:
            return True
    return False

def dig (N:int, M:int=-1, pr=None):
    M = N if M == -1 else M
    pr = pr or []
    if M == 0:
        print(*pr, sep="")
        return
    for num in range(1,N+1):
        if find(num, pr):
            continue
        pr.append(num)
        dig(N, M-1, pr)
        pr.pop()


dig(3)
