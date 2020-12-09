#create a program that asks the user to enter their name and age. Print out message addressed to them that tells them the year that they will turn 100 years old.
#Then ask user for another number and print out that many copies of the previous message
name = input("What is your name?  ")
age = input("What is your age?  ")
nage = int(age)
year = (100 - nage) + 2020
number = int(input("Please enter a number.  "))
a = ("Hello, {}! You will be 100 in year {}!".format(name.capitalize(), year))
for line in range(number):
    print(a)
