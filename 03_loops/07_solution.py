while True:
    number = int(input("Enter a number between 1 and 10: "))
    
    if 1 <= number <= 10:
        print("Hurray Correct Value!!")
        break
    else:
        print("Invalid number, try again!")