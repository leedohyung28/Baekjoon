def main() :
    N = input()
    num_list = []
    for _ in range(int(N)) :
        num_list += parse_num(input())
    num_list.sort()
    for i in num_list :
        print(i)
    
def parse_num(string) :
    
    num_list = []
    in_a_row = False
    num_string = ""
    number_example = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    
    for i in string :
        if i in number_example :
            in_a_row = True
            num_string += i
            
        elif in_a_row == True :
            num_list.append(int(num_string))
            in_a_row = False
            num_string = ""
    if in_a_row == True :
        num_list.append(int(num_string))
    
    return num_list

if __name__ == "__main__" :
    main()