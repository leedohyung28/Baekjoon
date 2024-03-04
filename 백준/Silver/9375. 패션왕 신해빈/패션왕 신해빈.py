import sys

tc = int(sys.stdin.readline().strip())

for _ in range(tc) :
    N = int(sys.stdin.readline().strip())
    clothing = dict()
    for i in range(N) :
        __, cloth_type = sys.stdin.readline().split()
        if cloth_type not in list(clothing.keys()) :
            clothing[cloth_type] = 1
        else :
            clothing[cloth_type] += 1
    result = 1
    for k in list(clothing.keys()) :
        result *= (clothing[k]+1)
    print(result-1)