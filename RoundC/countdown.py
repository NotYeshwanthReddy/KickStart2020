"""---------------------Base Code-------------------"""

# T = int(input())

# for _ in range(T):
#     N, K = [int(i) for i in input().split(' ')]
#     arr = list(map(int, input().split(" ")))
    
#     ints=0
#     countdowns = 0
#     temp = []
    
#     for i in arr:
#         if i==(K-ints):
#             ints+=1
#             temp.append(i)
#         if ints!=0 and i==1:
#             countdowns += 1
#             ints=0
#     print("Case #"+str(_+1)+": "+str(countdowns), temp)

"""---------------------Nested if-------------------"""

T = int(input())

for _ in range(T):
    N, K = [int(i) for i in input().split(' ')]
    arr = list(map(int, input().split(" ")))
    
    ints=0
    countdowns = 0
    temp = []
    index = []
    
    for ind, i in enumerate(arr):
        if i==K-ints:
            ints+=1
            temp.append(i)
            index.append(ind)
            if ints==K:
                ints=0
                countdowns+=1
        else:
            ints=0

    print("Case #"+str(_+1)+": "+str(int(countdowns)))
    print(temp, index)



"""---------------------String Stunt-------------------"""
# T = int(input())

# def getIndexes(strr, s): 
#     count = 0
#     for i in range(len(strr)): 
#         if (strr[i:i + len(s)] == s): 
#             count += 1
#     return count

# for _ in range(T):
#     N, K = [int(i) for i in input().split(' ')]
#     arr = ' ' + input() + ' '
    
#     strr = ' '
#     for i in range(K,0,-1):
#         strr += str(i)+' '
    
#     count = getIndexes(arr, strr)
    
#     # print(len(indexes))
#     print("Case #"+str(_+1)+": "+str(count))
