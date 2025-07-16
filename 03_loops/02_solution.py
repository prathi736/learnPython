n = input("Enter a number: ")
nInt = int(n)

sum_even = 0

for i in range(1, nInt+1):
    if i%2 == 0:
        sum_even += i

print("Sum of even number: ",sum_even)