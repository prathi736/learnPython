age = input("Please enter your age: ")

ageInt = int(age)

if ageInt < 13:
    print("Child")
elif ageInt < 20:
    print("Teenager")
elif ageInt < 60:
    print("Adult")
else:
    print("Senior")