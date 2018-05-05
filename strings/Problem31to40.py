# problem 31

print("--------------Problem 31 End--------------------------")

# problem 32


print("--------------Problem 32 End--------------------------")

# problem 33

print("--------------Problem 33 End--------------------------")

# problem 34

print("--------------Problem 34 End--------------------------")

# problem 35

x = 3000000
y = 30000000

print("Formatted Number with comma separator: "+"{:,}".format(x));
print("Formatted Number with comma separator: "+"{:,}".format(y));

print("--------------Problem 35 End--------------------------")

# problem 36
x = 0.25
y = -0.25
print("Formatted Number with percentage: "+"{:.2%}".format(x));
print("Formatted Number with percentage: "+"{:.2%}".format(y));
print("--------------Problem 36 End--------------------------")

# problem 37

x = 21
print("Left aligned :  {:<10d}".format(x))
print("Right aligned: {:10d}".format(x))
print("Center aligned:{:^10d}".format(x))
print("--------------Problem 37 End--------------------------")

# problem 38

str1 = 'The quick brown fox jumps over the lazy dog.'
print(str1.count("fox"))

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
