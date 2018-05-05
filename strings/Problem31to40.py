# problem 31

print("--------------Problem 31 End--------------------------")

# problem 32


print("--------------Problem 32 End--------------------------")

# problem 33

print("--------------Problem 33 End--------------------------")

# problem 34

print("--------------Problem 34 End--------------------------")

# problem 35

print("--------------Problem 35 End--------------------------")

# problem 36

print("--------------Problem 36 End--------------------------")

# problem 37

print("--------------Problem 37 End--------------------------")

# problem 38

print("--------------Problem 38 End--------------------------")


# problem 39

def reverse_string(str1):
    return ''.join(reversed(str1))


print(reverse_string("abcdef"))
print(reverse_string("Python Exercises."))

print("--------------Problem 39 End--------------------------")


# problem 40
def reverse_string_words(input):
    temp = ''
    for i in input.split():
        temp = ' ' + ''.join(reversed(i)) + temp
    return temp


print(reverse_string_words("The quick brown fox jumps over the lazy dog."))
print(reverse_string_words("Python Exercises."))

print("--------------Problem 40 End--------------------------")
