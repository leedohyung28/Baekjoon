import sys
import math

# 입력 받기
N = int(sys.stdin.readline())

# 내것보다 효율적인 dp -> 인터넷 보고 찾음
# max_num = 100_001
# dp = [max_num] * (N+1)
dp = [i for i in range(N+1)]

# 조금 더 빠른 검색을 위해
for k in range(1, N+1) :
    # 기존의 제곱은 찾되
    if math.sqrt(k) % 1 == 0 :
        dp[k] = 1
    
    else :
        # 제곱을 기준으로 for문 재구성 -> 인터넷 보고 찾음
        for j in range(1, k) :
            if j*j > k :    # 제곱이 숫자를 넘어버리면 바로 종료
                break
            # 제곱을 기준으로 dp 재계산
            if dp[k] > dp[k-j*j] + dp[j*j] :
                dp[k] = dp[k-j*j] + dp[j*j]

print(dp[N])