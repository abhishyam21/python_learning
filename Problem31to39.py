# problem 31


def compute_gcd(x, y):
    gcd = 1
    if x % y == 0:
        return y
    for k in range((y / 2), 0, -1):
        if x % k == 0 and y % k == 0:
            gcd = k
            break
    return gcd


print(compute_gcd(2, 5))
print(compute_gcd(12, 17))
print(compute_gcd(4, 6))
print("--------------Problem 31 End--------------------------")


# problem 32

def compute_lcm(x, y):
    z = max(x, y)

    while True:
        if z % x == 0 and z % y == 0:
            lcm = z
            break
        z = z + 1
    return lcm


print(compute_lcm(2, 5))
print(compute_lcm(15, 17))
print(compute_lcm(4, 6))

print("--------------Problem 32 End--------------------------")


# problem 33


def sum_of_numbers(x, y, z):
    if x == y or y == z or x == z:
        return 0
    else:
        return x + y + z


print(sum_of_numbers(2, 1, 2))
print(sum_of_numbers(1, 2, 3))
print(sum_of_numbers(1, 1, 1))
print("--------------Problem 33 End--------------------------")


# problem 34

def sum_of_two(x, y):
    z = x + y
    if 15 <= z <= 20:
        return 20
    else:
        return z


print(sum_of_two(10, 6))
print(sum_of_two(10, 2))
print(sum_of_two(10, 12))
print("--------------Problem 34 End--------------------------")


# problem 35


def test_number5(x, y):
    if x == y or (x + y) == 5 or abs(x - y) == 5:
        return True
    return False


print(test_number5(7, 2))
print(test_number5(3, 2))
print(test_number5(2, 2))
print("--------------Problem 35 End--------------------------")


# problem 36


def addNumbers(x, y):
    if isinstance(x, int) and isinstance(y, int):
        return x + y
    else:
        raise TypeError("Input Must be Integer")


print(addNumbers(1, 2))
# print(addNumbers("abc", 2))

print("--------------Problem 36 End--------------------------")


# problem 37

def personDetails():
    name = "Kiran Rao"
    age = 21
    address = "Bangalore, Karnataka, India"
    return "Name: {}\nAge: {}\nAddress: {}".format(name, age, address)


print(personDetails())

print("--------------Problem 37 End--------------------------")


# problem 38

def computeFormula(x, y):
    sum = x + y
    return sum * sum


print(computeFormula(4, 3))
print("--------------Problem 38 End--------------------------")

# problem 39

amt = 10000
int = 3.5
years = 7

future_value = amt * ((1 + (0.01 * int)) ** years)
print(round(future_value, 2))
print("--------------Problem 39 End--------------------------")

# problem 40
import math


def distanceBetweenPoints(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


print(distanceBetweenPoints(4, 0, 6, 6))
print("--------------Problem 40 End--------------------------")

# problem 6
print("--------------Problem 6 End--------------------------")

# problem 6
print("--------------Problem 6 End--------------------------")
