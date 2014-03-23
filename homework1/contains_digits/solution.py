def contains_digit(number, digit):
    while(number!=0):
        if number% 10 == digit:
            return True
            break
        else:
            number=number // 10
    else:
        return False
def contains_digits(number, digits):
    for i in digits:
        if contains_digit(number,i) == False:
            return False
            break
    return True