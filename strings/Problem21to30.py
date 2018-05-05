# problem 21

def to_uppercase(input):
    counter = 0
    for i in input[:4]:
        if i.upper() == i:
            counter += 1

    if counter >= 2:
        return input.upper()

    return input


print(to_uppercase('Python'))
print(to_uppercase('PyThon'))

print("--------------Problem 21 End--------------------------")

# problem 22


def lexicographi_sort(input):
    return sorted(input)


print(lexicographi_sort('w3resource'))
print(lexicographi_sort('QUqckbrown'))

print("--------------Problem 22 End--------------------------")

# problem 23

str1='Python Exercises\n'
print(str1)
print(str1.strip())

print("--------------Problem 23 End--------------------------")

# problem 24

string = "w3resource.com"
print(string.startswith("w3r"))

print("--------------Problem 24 End--------------------------")

# problem 25

def caesar_encrypt(text, step):
    pass


code = caesar_encrypt('abc', 2)
print()
print(code)
print()

print("--------------Problem 25 End--------------------------")

# problem 26

print("--------------Problem 26 End--------------------------")

# problem 27

print("--------------Problem 27 End--------------------------")

# problem 28

print("--------------Problem 28 End--------------------------")

# problem 29

print("--------------Problem 29 End--------------------------")

# problem 30
print("--------------Problem 30 End--------------------------")
