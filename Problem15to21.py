# problem 15
from math import pi

radius = float(raw_input("Enter Radius of the Sphere: "))
print("Area of the Sphere with Radius " + str(radius) + " is: " + str((4.0 / 3.0) * pi * radius ** 3))

print("--------------Problem 15 End--------------------------")

# problem 16
sampleNumber = int(raw_input("Enter a Number: "))


def difference(sampleNumber):
    if sampleNumber > 17:
        return (sampleNumber - 17) * 2
    else:
        return 17 - sampleNumber


print(difference(sampleNumber))
print("--------------Problem 16 End--------------------------")

# problem 17
sampleNumber = int(raw_input("Enter a Number: "))


def nearThousand(sampleNumber):
    return (abs(1000 - sampleNumber) <= 100) or (abs(2000 - n) <= 100)


print(nearThousand(sampleNumber))

print("--------------Problem 17 End--------------------------")


# problem 18

def sumThrice(x, y, z):
    if x == y == z:
        return x * 9
    else:
        return x + y + z


x = int(raw_input("Enter a number:"))
y = int(raw_input("Enter a number:"))
z = int(raw_input("Enter a number:"))

print(sumThrice(x, y, z))

print("--------------Problem 18 End--------------------------")

# problem 19
stringContent = raw_input("Enter any string: ")
if stringContent.startswith("is"):
    print(stringContent)
else:
    print("is" + stringContent)

print("--------------Problem 19 End--------------------------")

# problem 20
stringContent = raw_input("Enter any string to be repeated: ")
sampleNumber = int(raw_input("Enter a number:"))
stringContent = stringContent * 3
print(stringContent)

print("--------------Problem 20 End--------------------------")

# problem 21
sampleNumber = int(raw_input("Enter a number: "))
if sampleNumber % 2 == 0:
    print("Number is Even")
else:
    print("Number is Odd")

print("--------------Problem 21 End--------------------------")