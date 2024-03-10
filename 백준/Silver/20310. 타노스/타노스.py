import sys

input = list(sys.stdin.readline().strip())

dic = dict()
dic[0] = 0
dic[1] = 0
for i in input :
    if i == '0' :
        dic[0] += 1
    else :
        dic[1] += 1
        
result = dic[0]//2*str(0) + dic[1]//2*str(1)
print(result)