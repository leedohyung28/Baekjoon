import sys

N = int(sys.stdin.readline())
C = list(sys.stdin.readline().strip())

def cal(C, gate) :
    for i in range(0, len(gate), 2) :
        h = gate[i]
        t = gate[i+1]
        
        v = int(C[h])
        for k in range(h+1, t, 2) :
            if C[k] == '+' :
                v += int(C[k+1])
            elif C[k] == '-' :
                v -= int(C[k+1])
            else :
                v *= int(C[k+1])

            C[k] = None
            C[k+1] = None
        C[h] = v
    C = [x for x in C if x is not None]
    V = int(C[0])
    for k in range(1, len(C), 2) :
        if C[k] == '+' :
            V += int(C[k+1])
        elif C[k] == '-' :
            V -= int(C[k+1])
        else :
            V *= int(C[k+1])
    return V

def make_gate(N) :
    X = [x for x in range(0, N, 2)]
    gate = []
    for i in range(len(X)-1) :
        gate.append([X[i], X[i+1]])
        for k in gate :
            if X[i] not in k and X[i+1] not in k :
                gate.append(k+[X[i], X[i+1]])
                
    return gate

if N == 1 :
    print(C[0])
else :
    result = int(C[0])
    for k in range(1, len(C)-1, 2) :
        if C[k] == '+' :
            result += int(C[k+1])
        elif C[k] == '-' :
            result -= int(C[k+1])
        else :
            result *= int(C[k+1])
    gates = make_gate(N)
    for gate in gates :
        CC = C.copy()
        result = max(result, cal(CC, list(gate)))
    print(result)