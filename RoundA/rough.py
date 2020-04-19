T = int(input())
N, K, P = [0]*T, [0]*T, [0]*T
Stacks = [0]*N
for t in range(T):
    N[t], K[t], P[t] = list(map(int, input().split(" ")))
    for n in range(N[t]):
        Stacks[n] = (list(map(int, input().strip().split(" "))))


ans = []
for t in range(T):
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
    ans.append(sum(sol))

for t in range(T):
    print("Case #",t+1,": ",ans[t], sep="")
