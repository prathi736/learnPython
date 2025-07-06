input_string = input("Enter a string: ")

for  char in input_string:
    if input_string.count(char) == 1:
        print("First Non Repeated Character is:",char)
        break #for optimization purposes