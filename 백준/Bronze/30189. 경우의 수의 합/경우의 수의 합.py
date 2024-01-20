def main() :
    # 양의 정수 n, m은 띄어쓰기로 구분
    n, m = map(int, input().split())
    print (f(n,m,n+m))
    
def f(a,b,c) :
    # a + b = 0 일때,
    if c == 0 :
        # a = 0, b = 0 일 때 조건 하나만 성립
        return 1
    
    # a + b = 1, 2, ...
    else :
        result = 0
        for j in range(a+1) :
            for k in range(b+1) :
                # 성립할 때 result를 더해준다
                if j + k == c :
                    result += 1
                    
        # 시간 절약을 위해 재귀함수로 구현
        return f(a,b,c-1) + result
    
if __name__ =="__main__":
    main()