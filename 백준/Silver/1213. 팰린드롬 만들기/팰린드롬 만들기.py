import sys

letter_list = list(sys.stdin.readline().strip())
letter_list.sort()

letter_dict = dict()
for i in letter_list :
    if i not in list(letter_dict.keys()) :
        letter_dict.update({i: 1})
    else :
        letter_dict[i] += 1

odd = False
fin = False

result = ''
mid = ''
for k in letter_dict.keys() :
    v = letter_dict[k]
    if v % 2 != 0 :
        if odd :
            print("I'm Sorry Hansoo")
            fin = True
            break
        else :
            odd = True
            result += k * (v//2)
            mid = k
    else :
        result += k * (v//2)
if not fin :
    list_result = list(result)
    list_result.reverse()
    reversed_result = ''.join(list_result)
    result = result + mid + reversed_result
    print(result)