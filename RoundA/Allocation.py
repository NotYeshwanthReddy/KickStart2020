T = int(input())
N, B = [0]*T, [0]*T
A = [0]*T
for t in range(T):
    N[t], B[t] = list(map(int, input().split(" ")))
    A[t] = list(map(int, input().strip().split(" ")))

ans = []
for t in range(T):
    price_list = A[t]
    price_list.sort()
    budget = 0
    i=0
    while budget<=B[t]:
        budget+=A[t][i]
        i+=1
        # print(budget, i)
    ans.append(i-1)
    
for t in range(T):
    print("Case #",t+1,": ",ans[t], sep="")
