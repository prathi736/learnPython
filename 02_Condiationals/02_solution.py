age = input("Please enter your age: ")

ageInt = int(age)

day = input("Please enter current day: ")

price = 12 if ageInt >= 18 else 8

if day == "Wednesday":
    # price = price - 2
    price -= 2

print("Your Movie Ticket Price: $",price)