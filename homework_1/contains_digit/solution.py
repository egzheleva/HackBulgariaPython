def contains_digit(number, digit):
    while(number!=0):
        if number% 10 == digit:
            return True
            break
        else:
            number=number // 10
    else:
        return False