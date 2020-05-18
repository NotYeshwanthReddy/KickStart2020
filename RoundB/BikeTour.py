T = int(input())

for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split(" ")))
    
    i=0
    peaks = 0
    while(i+2<n):
        temp = arr[i+1]
        if temp>arr[i] and temp>arr[i+2]:
            peaks += 1
        i+=1
    print("Case #"+str(_+1)+": "+str(peaks))
