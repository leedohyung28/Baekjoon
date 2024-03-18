def solution(price, money, count):
    answer = 0
    for i in range(count, 0, -1) :
        answer += price * i
    return max(answer-money,0)