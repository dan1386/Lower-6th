
def toBinary(num):
    result = ""
    if num == 0:
        return 0
    
    while num != 0:
        rem = num % 2
        num = num //2
        result = str(rem) + result
    return result
print(toBinary(25))
        

        
