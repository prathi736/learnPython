marks = input("Please enter your marks: ")
marksInt = int(marks)

if marksInt >= 101:
    print("Please enter correct marks!")
    exit()

if marksInt >= 90:
    grade = "A"
    comment = "Great Marks!"
elif marksInt >= 80:
    grade = "B"
    comment = "Good Marks!"
elif marksInt >= 70:
    grade = "C"
    comment = "Average Marks!"
elif marksInt >= 60:
    grade = "D"
    comment = "Need to work hard!"
else:
    grade = "F"
    comment = "Better Luck Next Time!"

print("Your Grade:",grade)
print("Comment:",comment)