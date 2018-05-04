# problem 22


def countFours(x):
    counter = 0
    for i in x:
        if i == 4:
            counter = counter + 1
    return counter


print("4 is repeated " + str(countFours([1, 2, 3, 4, 5, 4, 7])) + " times")

print("--------------Problem 22 End--------------------------")


# problem 23


def substringCopy(sampleString, sampleNumber):
    length = len(sampleString)
    subStr = sampleString
    if length > sampleNumber:
        subStr = sampleString[: sampleNumber]

    return subStr * sampleNumber


sampleString = raw_input("Enter Some String: ")
sampleNumber = int(raw_input("Enter Some Number: "))
print(substringCopy(sampleString, sampleNumber))

print("--------------Problem 23 End--------------------------")


# problem 24

def isVowel(char):
    vowels = ('a', 'e', 'i', 'o', 'u')
    return vowels.__contains__(char)


print(isVowel('c'))
print(isVowel('a'))

print("--------------Problem 24 End--------------------------")


# problem 25

def is_group_member(list, x):
    return list.__contains__(x)


print(is_group_member([1, 5, 8, 3], 3))
print(is_group_member([5, 8, 3], -1))
print("--------------Problem 25 End--------------------------")


# problem 26

def histogram(list):
    for i in list:
        temp = ''
        for j in range(0, i):
            temp += "@ "
        print(temp)


histogram([2, 3, 6, 5])
print("--------------Problem 26 End--------------------------")


# problem 27

def concatinate(list):
    temp = ''
    for i in list:
        temp += str(i)
    return temp


print(concatinate([1, 5, 12, 2]))
print("--------------Problem 27 End--------------------------")

# problem 28

numbers = [
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 743, 527
]

for i in numbers:
    if i == 237:
        print(237)
        break
    else:
        if i % 2 == 0:
            print(i)

print("--------------Problem 28 End--------------------------")

# problem 29

color_list_1 = {"White", "Black", "Red"}
color_list_2 = {"Red", "Green"}

print(color_list_1.difference(color_list_2))

print("--------------Problem 29 End--------------------------")

# problem 30

base = int(raw_input("Enter base of the triangle: "))
height = int(raw_input("Enter height of the triangle: "))
print("Area of Triangle with Base " + str(base) + " and height " + str(height) + " is " + str(0.5 * base * height))

print("--------------Problem 30 End--------------------------")
