T = int(input())
Strings=[]

for _ in range(T):
    Strings.append(input())

for _ in range(T):
    w = 0
    h = 0
    String = Strings[_]
    
    stack = []
    Multiple = 1
    integer = 0
    for char in String:
        if char.isdigit():
            integer = (integer*10)+int(char)
        elif char=="(":
            stack.append(integer)
            Multiple *= integer
            integer = 0
        elif char==")":
            Multiple //= stack.pop()
        else:
            if char=="N":
                h -= Multiple
            elif char=="S":
                h += Multiple
            elif char == "W":
                w -= Multiple
            elif char == "E":
                w += Multiple
    w = int(w%1000000000)+1
    h = int(h%1000000000)+1
    print("Case #"+str(_+1)+": "+str(w)+" "+str(h))
