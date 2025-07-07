import math

def circle_values(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference

rad = int(input("Enter the radius of circle: "))

a, c = circle_values(rad)

print("Area:",round(a,2))
print("Circumference:",round(c,2))