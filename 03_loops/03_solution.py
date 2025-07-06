number = input("Enter a number: ")
numberInt = int(number)

for i in range(1,11):
    if i == 5:
        continue
    print(numberInt, "x", i, "=", numberInt*i)