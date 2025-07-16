# Lambda/anonymous function -> jin functions ka name nahi hota hai

# Normal function - used many times
# def cube(num):
#     return num ** 3
# print(cube(3))

# Lambda Function - used only one time, useful in frameworks
number = int(input("Enter a number: "))

cube = lambda x: x ** 3
result = cube(number)
print("Cube of the number:",result)