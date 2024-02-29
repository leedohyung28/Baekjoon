import sys

# 입력
letter_list = list(sys.stdin.readline().strip())
letter_list.sort()

# Dict로 각 글자별 개수 정리
letter_dict = dict()
for i in letter_list :
    if i not in list(letter_dict.keys()) :
        letter_dict.update({i: 1})
    else :
        letter_dict[i] += 1

odd = False     # 홀수가 2개 이상인지 체크
fin = False     # 반복문 탈출

result = ''     # 결과값
mid = ''        # 중간에 들어갈 수 있는 글자 (홀수개)

for k in letter_dict.keys() :
    v = letter_dict[k]
    if v % 2 != 0 :
        # 홀수개인 알파벳이 2개 이상이면 출력 후 탈출
        if odd :
            print("I'm Sorry Hansoo")
            fin = True
            break
        
        # 처음 홀수개인 알파벳이 나오면
        else :
            odd = True
            result += k * (v//2)    # v-1/2 만큼 result에 넣고
            mid = k                 # 중간에 글자 삽입
    
    # 짝수개인 알파벳은
    else :
        result += k * (v//2)        # v/2 만큼 result에 넣음

# I'm Sorry Hansoo 가 출력되지 않았으면
if not fin :
    # 글자 뒤집기
    reversed = result[::-1]
    
    # 글자 모두 합쳐서 출력
    result = result + mid + reversed
    print(result)