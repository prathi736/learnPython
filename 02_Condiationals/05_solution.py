weather = input("Please enter your current weather: ")

weatherLower = weather.lower()

if weatherLower == "sunny":
    activity = "Go for a walk"
elif weatherLower == "rainy":
    activity = "Read a book"
elif weatherLower == "snowy":
    activity = "Build a snowman"
else:
    activity = "Do Nothing, Just Chill"

print(weather, ":",activity)