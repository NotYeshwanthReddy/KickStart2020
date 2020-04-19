import math

T = int(input())
N, K = [0]*T, [0]*T
M = [0]*T
for t in range(T):
    N[t], K[t] = list(map(int, input().split(" ")))
    M[t] = list(map(int, input().strip().split(" ")))


ans = []
for t in range(T):
    diff_arr = []
    for i in range(len(M[t])-1):
        diff_arr.append(M[t][i+1]-M[t][i])
    print(diff_arr)

    for k in range(K[t]):
        diff_arr.sort()
        temp = diff_arr.pop()
        temp = [temp//2, temp//2] if (temp/2)%2==0 else [temp//2-1, (temp//2)+1]
        diff_arr.extend(temp)
        print(k, diff_arr)
    
    diff_arr.sort()
    print(diff_arr)
    ans.append(diff_arr[-1])

for t in range(T):
    print("Case #",t+1,": ",ans[t], sep="")
