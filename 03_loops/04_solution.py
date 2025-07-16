input_string = input("Enter a string:")
reverse_string = ""

for char in input_string:
    reverse_string = char + reverse_string

print("Reverse of input string:",reverse_string)