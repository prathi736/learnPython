order_size = input("Please enter your coffee size: ")
orderLower = order_size.lower()

extra_shot = bool(input("Enter True or Left Empty: "))

if extra_shot:
    coffee = orderLower + " coffee with an extra shot"
else:
    coffee = orderLower + " coffee"

print("Your Order: ",coffee)