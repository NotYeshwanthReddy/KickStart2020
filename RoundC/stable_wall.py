def IsStable(matrix, repl, ch):
    isStable = True
    prevIndeces = set([])
    for row in range(len(matrix)):
        matrix[row] = matrix[row].replace(repl, ch)
        if(isStable):
            indices = set([i for i, x in enumerate(matrix[row]) if x == ch])
            if(len(prevIndeces.difference(indices)) > 0):
                isStable = False
            prevIndeces = indices
    return matrix, isStable

def Recursion(matrix, alphabet, seq):
    
    alphabet = alphabet.difference(set(seq))
    print("----------",seq, alphabet)
    bol = None

    if alphabet==None:
        return True, seq

    for alp in alphabet:
        matrix, isStable = IsStable(matrix, seq[0], alp)
        if isStable:
            seq.append(alp)
            bol,seq = Recursion(matrix, alphabet, seq)
        else:
            return False, -1
    return bol, seq


T = int(input())

for _ in range(T):
    # Input
    R, C = [int(i) for i in input().split(' ')]
    
    alphabet = set()
    stable = []
    matrix = []
    ans = -1
    
    for i in range(R):
        line = str(input())
        matrix.append(line)
        alphabet = alphabet.union(set(line))

    # Code
    for alp in alphabet:
        if IsStable(matrix, alp, alp):
            bol, seq = Recursion(matrix, alphabet, [alp])

    if bol:
        print("Case #"+str(_+1)+": "+"".join(seq))
    else:
        print("Case #"+str(_+1)+": -1", bol, seq)
