# problem 41

def stript_chars(input):
    return "".join(i for i in input if i not in ['a', 'e', 'i', 'o', 'u'])


print(stript_chars("The quick brown fox jumps over the lazy dog."))

print("--------------Problem 41 End--------------------------")

# problem 42
import collections


def char_count(input):
    dict = collections.defaultdict(int)
    for i in input:
        dict[i] += 1
    for i in dict:
        if dict[i] > 1:
            print("%s -> %i" % (i, dict[i]))


char_count('thequickbrownfoxjumpsoverthelazydog')

print("--------------Problem 42 End--------------------------")

# problem 43

area = 1256.66
volume = 1254.725
decimals = 2
print("The area of the rectangle is {0:.{1}f}cm\u00b2".format(area, decimals))
decimals = 3
print("The volume of the cylinder is {0:.{1}f}cm\u00b3".format(volume, decimals))

print("--------------Problem 43 End--------------------------")


# problem 44

def pos_print(input):
    for i in range(0, len(input)):
        print("%s at position %i" % (input[i], i))


pos_print("abhishyam")

print("--------------Problem 44 End--------------------------")


# problem 45

def has_all_albets(input):
    return len(set(input.lower())) >= 26


print(has_all_albets("The quick brown fox jumps over the lazy dog"))
print(has_all_albets("The quick brown fox jumps over the lazy cat"))

print("--------------Problem 45 End--------------------------")

# problem 46


def convert_to_list(input):
    return input.split()


print(convert_to_list("The quick brown fox jumps over the lazy dog"))
print(convert_to_list("The quick brown fox jumps over the lazy cat"))

print("--------------Problem 46 End--------------------------")

# problem 47

print("--------------Problem 47 End--------------------------")

# problem 48


print("--------------Problem 48 End--------------------------")


# problem 49
def vowel1(input):
    return input.count('a') + input.count('e') + input.count('i') + input.count('o') + input.count('u')


def vowel2(text):
    vowels = "aeiuoAEIOU"
    return len([letter for letter in text if letter in vowels])


print(vowel1('w3resource'))
print(vowel2('w3resource'))

print("--------------Problem 49 End--------------------------")

# problem 50
str = "w,3,r,e,s,o,u,r,c,e"

print(str.split(',', 1))
print(str.split(',', 3))
print(str.rsplit(',', 1))
print(str.rsplit(',', 3))

print("--------------Problem 50 End--------------------------")
