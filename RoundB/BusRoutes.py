T = int(input())
for _ in range(T):
    n, d = [int(i) for i in input().split(' ')]
    busArr = [int(i) for i in input().split(' ')]
    busArr.reverse()
    ans = -1
    while(d >= 0):
        while(d % busArr[0] == 0):
            if(len(busArr) == 1):
                ans = d
                break;
            del busArr[0]
        if(ans != -1):
            break;
        d -= d%busArr[0]
    print("Case #"+str(_+1)+": "+str(ans))
