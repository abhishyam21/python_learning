# problem1

print("Length of 'abcd' is: " + str(len("abcd")))
print("Length of '' is: " + str(len("")))
print("Length of '-=123' is: " + str(len("-=123")))

print("--------------Problem 1 End--------------------------")


# problem2

def cal_char_frequency(input):
    dict = {}
    for i in input:
        keys = dict.keys()
        if i in keys:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict


print("Character Frequency of 'abhishyam' is:{} ".format(cal_char_frequency("abhishyam")))
print("Character Frequency of 'www.google.com' is:{} ".format(cal_char_frequency("www.google.com")))

print("--------------Problem 2 End--------------------------")


# problem 3

def string_both_ends1(input):
    str_len = len(input)
    if str_len < 2:
        return ''
    temp = ''
    for i in range(0, 2, 1):
        temp += input[i]
    for i in range(str_len - 2, str_len, 1):
        temp += input[i]
    return temp


def string_both_ends2(input):
    str_len = len(input)
    if str_len < 2:
        return ''
    return input[:2] + input[-2:]


print(string_both_ends1("abhishyam"))
print(string_both_ends1('w3resource'))
print(string_both_ends1('w3'))
print(string_both_ends1('w'))

print(string_both_ends2("abhishyam"))
print(string_both_ends2('w3resource'))
print(string_both_ends2('w3'))
print(string_both_ends2('w'))

print("--------------Problem 3 End--------------------------")


# problem 4

def change_char(input):
    temp = input
    first_char = input[:1]
    temp = temp.replace(first_char, "$")
    temp = first_char + temp[1:]
    return temp


print(change_char("abababa"))
print(change_char('restart'))

print("--------------Problem 4 End--------------------------")


# problem 5

def chars_mix_up(x, y):
    temp1 = y[:2] + x[2:]
    temp2 = x[:2] + y[2:]
    return temp1 + " " + temp2


print(chars_mix_up('abc', 'xyz'))

print("--------------Problem 5 End--------------------------")

# problem 6

print("--------------Problem 6 End--------------------------")

# problem 7

print("--------------Problem 7 End--------------------------")

# problem 8

print("--------------Problem 8 End--------------------------")

# problem 9

print("--------------Problem 9 End--------------------------")

# problem 10

print("--------------Problem 10 End--------------------------")
