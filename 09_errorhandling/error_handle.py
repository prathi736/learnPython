# Old way of opening the file
file = open("test.txt", 'w')
# w -> used to write in the file and it also creates the file, if file does not exist before writing in it

try:
    file.write("Learning python")
finally:
    file.close()

# New way of opening the file (automatically handles closing of file after writing)
with open("test.txt", 'w') as file:
    file.write("Learning python again")