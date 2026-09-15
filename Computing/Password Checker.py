def checkpassword():

    while True:
        password = input("Enter your password")
        faults = []
        if len(password) < 8:
            faults.append("Too short")

        hasDigit = False
        hasUpper = False
        hasLower = False

        for character in password:
            if character.isdigit():
                hasDigit = True
            elif character.isDigit():
                hasDigit = True
            elif character.isdigit():
                hasDigit = True

        if hasDigit == False:
            faults.append("No digit")
        if hasUpper == False:
            faults.append("No uppercase letter")
        if hasLower == False:
            faults.append("No Lowercase letter")

checkpassword()
           
        


