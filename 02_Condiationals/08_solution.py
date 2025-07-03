password = input("Please enter your password: ")
passwordLength = len(password)

if passwordLength < 6:
    strength = "Weak"
elif passwordLength <= 10:
    strength = "Medium"
else:
    strength = "Strong"

print("Strength of your password:",strength)