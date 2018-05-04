# problem 7
sampleText = raw_input("Enter Some file name with extension: ")
sampleList = sampleText.rsplit(".", 1)
print(sampleList[1])

print("--------------Problem 7 End--------------------------")

# problem 8
color_list = ["Red", "Green", "White", "Black"]
print("First Color: " + color_list[0])
print("Last Color: " + color_list[-1])

print("--------------Problem 8 End--------------------------")

# problem 9
exam_st_date = (11, 12, 2014)
print("Examination will start from : %i / %i / %i" % exam_st_date)

print("--------------Problem 9 End--------------------------")

# problem 10
sampleNumber = int(raw_input("Enter a number:"))
n1 = int("%s" % sampleNumber)
n2 = int("%s%s" % (sampleNumber, sampleNumber))
n3 = int("%s%s%s" % (sampleNumber, sampleNumber, sampleNumber))
print("Value of n+nn+nnn : " + str(n1 + n2 + n3))

print("--------------Problem 10 End--------------------------")

# problem 11
print(abs.__doc__)

print("--------------Problem 11 End--------------------------")

# problem 12
import calendar

year = int(raw_input("Enter Year:"))
month = int(raw_input("Enter month:"))
print(calendar.month(year, month))

print("--------------Problem 12 End--------------------------")

# problem 13
print(""""a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example""")

print("--------------Problem 13 End--------------------------")

import datetime

# problem 14
day1 = datetime.date(2017, 04, 01)
day2 = datetime.date(2018, 04, 01)
delta = day2 - day1
print(delta.days)

print("--------------Problem 14 End--------------------------")
