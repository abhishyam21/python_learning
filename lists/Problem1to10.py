# problem1

def sum_list(input):
    sum = 0
    for i in input:
        sum += i
    return sum


input = [1, 2, -8]
print(sum_list(input))
print(sum(input))
print(sum([x for x in input]))

print("--------------Problem 1 End--------------------------")


# problem2

def mutiply(input):
    sum = 1
    for i in input:
        sum *= i
    return sum


input = [1, 2, -8]

print(mutiply(input))
print([i * i for i in input])

print("--------------Problem 2 End--------------------------")


# problem 3

def max_num_in_list(input):
    max = 0
    for i in input:
        max = max if max > i else i
    return max


print(max_num_in_list([1, 2, -8, 0]))

print("--------------Problem 3 End--------------------------")


# problem 4

def smallest_num_in_list(input):
    min = input[0]
    for i in input:
        min = min if min < i else i
    return min


print(smallest_num_in_list([1, 2, -8, 0]))

print("--------------Problem 4 End--------------------------")


# problem 5

def match_words(input):
    counter = 0
    for i in input:
        if len(i) > 1 and i[0] == i[-1]:
            counter += 1
    return counter


print(match_words(['abc', 'xyz', 'aba', '1221']))

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
