def even_generate(limit):
    for i in range(2, limit + 1, 2):
        yield i # this works same as static in c and c++ programming 
    

number = int(input("Enter a number: "))

for num in even_generate(number):
    print(num)