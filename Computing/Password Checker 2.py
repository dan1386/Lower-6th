def checkpassword():

    while True:
        password = input("Enter your password: ")
        faults = []
        
        
        if len(password) < 8:
            faults.append("too short")

        hasDigit = False
        hasUpper = False
        hasLower = False

    
        for character in password:
            if character.isdigit():
                hasDigit = True
            if character.isupper():
                hasUpper = True
            if character.islower():
                hasLower = True

        
        if hasDigit == False:
            faults.append("no digit")
        if hasUpper == False:
            faults.append("no uppercase letter")
        if hasLower == False:
            faults.append("no lowercase letter")

    
        if len(faults) == 0:
            print("Password accepted")
            break  
        else:
            
            print(faults)


checkpassword()
