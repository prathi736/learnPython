fruit = "Banana"
color = input("Please enter color of the fruit: ")
colorLower = color.lower()

if fruit == "Banana":
    if colorLower == "green":
        print("Unripe")
    elif colorLower == "yellow":
        print("Ripe")
    elif colorLower == "brown":
        print("Overripe")
    else:
        print("No Information!")
else:
    print("Currently No Information about this fruit!")