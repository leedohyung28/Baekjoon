import sys

input = sys.stdin.readline().strip()

n = len(input)
count_a = input.count('a')

min_value = 1000
input += input
for i in range(len(input)//2) :
    if min_value > input[i:i+count_a].count('b') :
        min_value = input[i:i+count_a].count('b')
    
print(min_value)