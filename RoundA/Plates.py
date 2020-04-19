T = int(input())
N, K, P = [0]*T, [0]*T, [0]*T
Stacks = [0]*T
for t in range(T):
    N[t], K[t], P[t] = list(map(int, input().split()))
    temp = []
    for n in range(N[t]):
        temp.append((list(map(int, input().strip().split()))))
    Stacks[t] = temp

ans = []
for t in range(T):
    sol = []
    for i in range(P[t]):
        maxx=0
        maxx_i=0
        for j in range(N[t]):
            if len(Stacks[t][j])<P[t]-1:
                if maxx<sum(Stacks[t][j][:]):
                    (maxx, maxx_i) = (sum(Stacks[t][j][:]),j)
                elif maxx==sum(Stacks[t][j][:]) and Stacks[t][maxx_i][0]<=Stacks[t][j][0]:
                    (maxx, maxx_i) = (sum(Stacks[t][j][:]),j)
                else:
                    pass
            else:
                if maxx<sum(Stacks[t][j][:P[t]-i]):
                    (maxx, maxx_i) = (sum(Stacks[t][j][:P[t]-i]),j)
                elif maxx==sum(Stacks[t][j][:P[t]-i]) and Stacks[t][maxx_i][0]<=Stacks[t][j][0]:
                    (maxx, maxx_i) = (sum(Stacks[t][j][:P[t]-i]),j)
                else:
                    pass
        print(maxx_i, Stacks[t][maxx_i])
        sol.append(Stacks[t][maxx_i].pop(0))
    print(sol)
    ans.append(sum(sol))

for t in range(T):
    print("Case #",t+1,": ",ans[t], sep="")

"""
P = 5
N = 2
K = 4
Stacks = [[10,10,100,30],[80,50,10,50]]
# Stacks = [[1,2,3,100,5],[6,3,2,10,0]]
sol = []
for i in range(P):
    maxx=0
    maxx_i=0
    for j in range(N):
        if len(Stacks[j])<P-1:
            (maxx, maxx_i) = (sum(Stacks[j][:]),j) if maxx<sum(Stacks[j][:]) else (maxx, maxx_i)
        else:
            (maxx, maxx_i) = (sum(Stacks[j][:P-i]),j) if maxx<sum(Stacks[j][:P-i]) else (maxx, maxx_i)
    sol.append(Stacks[maxx_i].pop(0))
print(sum(sol))
"""