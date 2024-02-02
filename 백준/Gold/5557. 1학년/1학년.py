import sys

N = int(sys.stdin.readline())
numList = list(map(int, sys.stdin.readline().split()))
result = 0

answer = numList[-1]    # 합을 answer

# Dynamic Programming
# dp[a][b] => (a-1)번째 숫자까지의 합이 b인 경우
dp = [[0] * 21 for _ in range(N)]
dp[0][numList[0]] = 1   # 첫번째 숫자는 numList[0]일 때 한가지

# 전체 숫자를 Top-Down으로 반복
for i in range(1, N-1) :
    # 합이 0~20까지인 경우 모두 계산
    for j in range(21) :
        # 그 전에 존재하는 숫자가 0이 아니고 합이 20보다 작을 때
        if dp[i-1][j] != 0 and numList[i] + j <= 20:
            # (i-1)번째 DP 갱신
            dp[i][numList[i]+j] += dp[i-1][j]
        # 차의 경우도 DP 갱신
        if dp[i-1][j] != 0 and j - numList[i] >= 0 :
            dp[i][j-numList[i]] += dp[i-1][j]
print(dp[N-2][answer])