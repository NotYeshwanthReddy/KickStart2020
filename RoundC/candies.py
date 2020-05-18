T = int(input())

def Querry(candies, l, r):
    # mul = 1, add = 1
    res = 0
    for i in range(l-1, r):
        # res += candies[i] * mul 
        # mul *= -1
        if (i-l+1)%2!=0:
            res += (-1)*candies[i]*(i-l+2)
        else:
            res += candies[i]*(i-l+2)
    return res


for _ in range(T):
    N, Q = [int(i) for i in input().split(' ')]
    candies = list(map(int, input().split(" ")))
    print("-------------------------\n",candies)
    res = 0
    for i in range(Q):
        line = input().split(' ')
        if(line[0] == 'Q'):
            val = Querry(candies, int(line[1]), int(line[2]))
            res += val
            print(val, int(line[1]), int(line[2]))
        else:
            candies[int(line[1])-1] = int(line[2])
            print("U", candies)
    print("Case #"+str(_+1)+": "+str(int(res)))
