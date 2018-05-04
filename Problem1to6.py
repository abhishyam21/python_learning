# problem1
text = "Twinkle, twinkle, little star,\n \t\tHow I wonder what you are! \n\t\t\t\tUp above the world so high,\n\t\t\t\tLike a diamond in the sky.\n Twinkle, twinkle, little star,\n\t\t How I wonder what you are"
print(text)
print("--------------Problem 1 End--------------------------")
# problem2
import sys

print("Python version:")
print(sys.version)
print("Version info.")
print(sys.version_info)

print("--------------Problem 2 End--------------------------")

# problem 3
import datetime

print("Current Date")
print(datetime.datetime.now())

print("--------------Problem 3 End--------------------------")

# problem 4
import math

radius = float(raw_input("Enter Radius of the Circle"))
print("Area of the circle with radius " + str(radius) + " is: " + str(math.pi * radius ** 2))

print("--------------Problem 4 End--------------------------")

# problem 5
firstName = raw_input("Enter FirstName:")
lastName = raw_input("Enter LastName:")
print("Hello " + lastName + " " + firstName)

print("--------------Problem 5 End--------------------------")

# problem 6
temp = raw_input("Enter some , separated values:")
sampleList = temp.split(",", -1)
sampleTuple = tuple(sampleList)
print("List Content", sampleList)
print("Tuple Content", sampleTuple)

print("--------------Problem 6 End--------------------------")
