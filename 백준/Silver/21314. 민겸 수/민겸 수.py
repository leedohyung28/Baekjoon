import sys

input = list(sys.stdin.readline().strip())

most_num = ''
least_num = ''

M_most = 0
M_least = False
for i in input :
    if i == 'M' :
        
        if not M_least :
            M_least = True
            least_num += '1'
        else :
            least_num += '0'
        
        M_most += 1
        
    else :
        M_least = False
        least_num += '5'
        
        if M_most == 0 :
            most_num += '5'
        else :
            most_num += '5'
            most_num += '0' * M_most
            M_most = 0
    
if M_most != 0 :
    most_num += '1' * (M_most)
            
print(most_num)
print(least_num)