import sys

# 입력 받기
H, W = map(int, sys.stdin.readline().split())

cloud_map = []

for _ in range(H) :
    cloud_map.append(list(sys.stdin.readline().rstrip()))


# 순서대로 출력
for i in range(H) :
    time = 0                # 구름이 오는 시간 (기본값 0)
    cloud_coming = False    # 구름 접근 여부 (기본값 False)
    for k in range(W) :        
        if cloud_map[i][k] == 'c' : # 구름이라면
            time = 0                # 구름이 오는 시간 0으로 초기화
            print(time, end=' ')    # 출력
            cloud_coming = True     # 구름 접근 여부 -> True
        
        elif cloud_coming is True : # 구름이 접근 중이라면
            time += 1               # 접근 시간 + 1
            print(time, end=' ')    # 출력
        
        else :                      # 구름 X & 구름 접근 중 X
            print(-1, end=' ')      # 출력
    print() # 줄바꿈