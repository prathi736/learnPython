number = input("Enter a number: ")
numberInt = int(number)

factorial = 1

while numberInt > 0:
    # factorial = factorial * numberInt
    # numberInt = numberInt - 1
    factorial *= numberInt
    numberInt -= 1

print("Factorial of a given number:",factorial)