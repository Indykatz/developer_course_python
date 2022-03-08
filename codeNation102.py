# Code Nation: Developing Code

# Day Two

# Variables
print("--------------------------------------------------------")
print("VARIABLES")
print("---------")

# String 'str' - a word or sentence
a_string = "I AM A STRING"
print(type(a_string)) # NOT COVERED BUT HELPED ME SEE/UNDERSTAND
print(a_string)
print("")

# Integer 'int' - a whole number
an_int = 100
print(type(an_int)) # NOT COVERED BUT HELPED ME SEE/UNDERSTAND
print(an_int)
print("")

# Float 'float' - a decmimal point number
a_float = 1.00
print(type(a_float)) # NOT COVERED BUT HELPED ME SEE/UNDERSTAND
print(a_float)
print("")

# None 'NoneType' - none type 
a_none = None
print(type(a_none)) # NOT COVERED BUT HELPED ME SEE/UNDERSTAND
print(a_none)
print("")

# Boolen 'bool' - a True or False
a_bool = True
print(type(a_bool)) # NOT COVERED BUT HELPS SEE/UNDERSTAND
print(a_bool)
print("")

print("--------------------------------------------------------")
# Using variables in strings
print("USING VARIABLES IN STRINGS")
print("--------------------------")

# Fav drink variable
str_var = ("string")
print("Using variables inside a", str_var)
print("Using variables inside a " + str_var) # Alternative way (concat) 
print("")

# formatting string
a_var = "variables"
a_str = "format" 
print("Using {} with {}".format(a_var, a_str))
print("")

# f method
f_var = "f"
method_var = "method"
print(f"This is the {f_var} {method_var}")
print("")

# using 's in strings with variables
apos_var = "'"
print(f"This is how to use words\'s with an {apos_var}")
print("")

# New Line
print(f"Printing \n on \n new \n lines")
print("")

print("--------------------------------------------------------")
# Maths
print("MATHS")
print("-----")

a_var = 10
b_var = 20
# add
print(a_var + b_var)
# sub
print(a_var - b_var)
# multiply
print(a_var * b_var)
# div
print(a_var / b_var)
# power of 
print(a_var ** b_var)
# modula (remainder)
print(a_var % b_var)

print("--------------------------------------------------------")
# Putting into practce using user input
print("EXAMPLES USING USER INPUT")
print("-------------------------")

a_name = input("What is your name: ")
balance = 100

withdraw = int(input(f"Hello {a_name} how much do you want to withdraw?: "))
balance -= withdraw # balance will decrease by withdraw amount
print(balance)

credit = int(input(f"Hello {a_name} how much do you want to deposit?: "))
balance += credit # balance will increase by credit amount
print(balance)

print("--------------------------------------------------------")
# If else statements
print("IF ELFI ELSE WITH COMPARISONS")
print("-----------------------------")

my_var = 50

if a_var == 50:
    print(f"{a_var} is equal to than 50")
elif a_var < 100: 
    print(f"{a_var} is less than 100")
elif a_var > 10:
    print(f"{a_var} is greater than 10")
else:
    print(f"{a_var} is equal to 100")

# != not equal
# >= greater than or equal to
# <= less than or equal to
