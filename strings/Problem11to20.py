# problem 11

def remove_odd_index(input):
    temp = ''
    for i in range(0, len(input), 2):
        temp += input[i]
    return temp


print(remove_odd_index("abhishyam"))
print(remove_odd_index("ki"))
print(remove_odd_index('abcdef'))
print(remove_odd_index('python'))

print("--------------Problem 11 End--------------------------")


# problem 12
def count_of_words(input):
    dict = {}
    for i in input.split():
        keys = dict.keys()
        if i in keys:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict


print(count_of_words("hi how are you dear hi i am fine how are you"))
print(count_of_words('the quick brown fox jumps over the lazy dog.'))

print("--------------Problem 12 End--------------------------")

# problem 13

str = 'abhiSHyam'
print(str.upper())
print(str.lower())

print("--------------Problem 13 End--------------------------")

# problem 14


list = ['red', 'white', 'black', 'red', 'green', 'black']


def unique_words(list):
    result = set(list)
    result = sorted(result)
    return result


print(unique_words(list))

print("--------------Problem 14 End--------------------------")


# problem 15
def add_tags1(tag, input):
    return '<' + tag + '>' + input + '</' + tag + '>'


print(add_tags1('i', 'Python'))
print(add_tags1('b', 'Python Tutorial'))


def add_tags2(tag, input):
    return '<%s>%s</%s>' % (tag, input, tag)


print(add_tags2('i', 'Python'))
print(add_tags2('b', 'Python Tutorial'))

print("--------------Problem 15 End--------------------------")


# problem 16

def insert_sting_middle(str, word):
    return str[:2] + word + str[2:]


print(insert_sting_middle('[[]]', 'Python'))
print(insert_sting_middle('{{}}', 'PHP'))
print(insert_sting_middle('<<>>', 'HTML'))

print("--------------Problem 16 End--------------------------")


# problem 17

def insert_end(input):
    temp = input[-2:]
    return temp * 4


print(insert_end('Python'))
print(insert_end('Exercises'))

print("--------------Problem 17 End--------------------------")


# problem 18

def first_three(input):
    if len(input) < 3:
        return input
    else:
        return input[0:3]


print(first_three('ipy'))
print(first_three('python'))
print("--------------Problem 18 End--------------------------")


# problem 19

def last_char(input, seperator):
    list = input.rsplit(seperator, 1)
    return list[-1]


print(last_char("https://www.w3resource.com/python-exercises", '/'))
print(last_char("https://www.w3resource.com/python", '.'))

print("--------------Problem 19 End--------------------------")


# problem 20

def reverse_string(input):
    length = len(input)
    if length % 4 == 0:
        return ''.join(reversed(input))
    else:
        return input


print(reverse_string("abhishya"))
print(reverse_string('abcd'))
print(reverse_string('python'))

print("--------------Problem 20 End--------------------------")
