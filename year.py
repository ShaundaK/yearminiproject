#create a program that asks the user to enter their name and age. Print out message addressed to them that tells them the year that they will turn 100 years old.
#Then ask user for another number and print out that many copies of the previous message
def year_til(name, year):
    return "Hello " + name.capitalize() + "! You will be 100 in year " + str(year) + " !"
name = input("What is your name?  ")
age = input("What is your age?  ")
#number = int(input("Please enter a random number.  "))
nage = int(age)
year1 = (100 - nage) + 2020
result = year_til(name, year1)
print(result)
