# Code Nation: Developing Code

# Day Three
print("--------------------------------------------------------")

# Functions
print("FUNCTIONS")
print("---------")


# defining a function
def a_function():
    print("This is a function")
    print("")
# run a_function
a_function()

# Functions with parameters
def sum_function(num1, num2):
    num3 = num1 + num2
    print(f"The sum of {num1} and {num2} is {num3} using a function with parameters")
    print("")
# run sum_function
sum_function(1, 2)

# Global varibales
print("GLOBAL VARIABLES")
print("----------------")

balance = 1000

def cashWithdraw(amount, accNum):
    global balance
    print(f"Account {accNum} balance is {balance}")
    balance -= amount
    print(f"Account {accNum} new balance is {balance}")

cashWithdraw(100, "ABC1234")
cashWithdraw(200, "ABC1234")

print("")

# functions using in functions (recursive)
print("RETURN FUNCTIONS IN FUNCTIONS")
print("-----------------------------")

def multiply_by_nine_fifths(celsius): 
 return celsius * (9/5)
def get_fahrenheit(celsius):
 return multiply_by_nine_fifths(celsius) + 32
print("The temperature is {}°F".format(get_fahrenheit(15)))
#Output: The temperature is 59°F

get_fahrenheit(95)
print("")

# My example 
def a_sum():
    num1 = int(input("please enter number... "))
    num2 = int(input("please enter number... "))
    return num1 + num2

def power_of():
    num3 = a_sum()
    num4 = num3 ** 2
    print(num4)

power_of()

print("")

# AND OR
print("AND OR")
print("------")

a_var = 20
if a_var > 10 and a_var< 100:
    print("And statements")

if a_var < 10 or a_var > 15:
    print("Or statement ")
