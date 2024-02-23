import sys

def check_quater(sX, eX, sY, eY, vid) :
    standard_num = vid[sY][sX]
    for y in range(sY, eY) :
        for x in range(sX, eX) :
            if standard_num != vid[y][x] :
                mX = (sX + eX) // 2
                mY = (sY + eY) // 2
                
                n1 = check_quater(sX, mX, sY, mY, vid)
                n2 = check_quater(mX, eX, sY, mY, vid)
                n3 = check_quater(sX, mX, mY, eY, vid)
                n4 = check_quater(mX, eX, mY, eY, vid)
                return str('('+n1+n2+n3+n4+')')
    return str(standard_num)

def main() :
    N = int(sys.stdin.readline().strip())
    video = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
    result = check_quater(0,N,0,N,video)
    print(result)
    
if __name__ == "__main__" :
    main()