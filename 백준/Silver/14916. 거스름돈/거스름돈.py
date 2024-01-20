def main() :
    strInput = input()
    intInput = int(strInput)
    
    if intInput == 1 or intInput == 3 :
        print(-1)
        
    else :
        result = 0
        five_won = intInput // 5
        rest = intInput % 5
        if rest % 2 == 0 :
            result = int(five_won + rest / 2)
        else :
            result = int(five_won - 1 + (rest+5)/2)
        
        print(result)
    
if __name__ == "__main__" :
    main()