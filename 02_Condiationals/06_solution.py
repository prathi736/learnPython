distance = input("Please enter your travel distance: ")
distanceInt = int(distance)

if distanceInt < 3:
    transport = "Walk"
elif distanceInt <= 15:
    transport = "Bike"
else:
    transport = "Car"

print("Recommended Transport:",transport)