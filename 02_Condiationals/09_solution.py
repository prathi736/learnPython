year = input("Enter a year: ")
yearInt = int(year)

if (yearInt % 400 == 0) or (yearInt % 4 == 0 and yearInt % 100 !=0):
    print(yearInt, "is a Leap Year")
else:
    print(yearInt, "is Not a Leap Year")