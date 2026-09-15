
print(" Starting Game ... Enter Numbers 1 -100 ")

for i in range(1,101):
    if i % 3 == 0 and i % 5 ==0:
        correct = "FizzBuzz"
    elif i % 5 == 0:
        correct = "Buzz"
    elif i % 3 ==0:
        correct = 'Fizz'
    else:
        correct = str(i)

    num = input()
    if num != correct:
        print("Error! the correct answer = ", correct)
    


        

    
