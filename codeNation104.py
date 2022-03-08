# Code Nation: Developing Code

# Day four
print("--------------------------------------------------------")

# Lists
print("LIST")
print("----")

# create alist usimg []
a_list = [
    "apples", "pears", "kiwi"
    ]
print(a_list)
print("")

b_list = ["milk", "coffee"]
print(b_list)
print("")

# add item to list
a_list.append("peach")
print(a_list)
print("")

# combine two lists
c_list = a_list + b_list
print(c_list)
print("")

# length of list
print(len(c_list))
print("")

# Index List
print(c_list[0])
print("")

# Change list item
c_list[0] = "oranges"
print(c_list)
print("")

# Remove last item in list
c_list.pop()
print(c_list)
print("")

# pop index value             
c_list.pop(0)
print(c_list)
print("")

# seperate list values
print(*c_list, sep=" ")
print("")

# remove() - removes item from list
c_list.remove("pears")
print(c_list)
print("")

# reverse() - reverse list order
c_list.reverse()
print(c_list)
print("")

# sort() - sort acceding 
c_list.sort()
print(c_list)
# sort() - sort decending 
c_list.sort(reverse = True)
print(c_list)
print("")

# count() - counts occurences of value
print(c_list.count("kiwi"))
print("")

# extend()- extends list by appending items from another list 
d_list = ["dog food", "cat food"]
c_list.extend(d_list)
print(c_list)

# insert
c_list.insert(0, "chocolate")
print(c_list)


# ---------------------------------------

# turle - immutable list (cant change) = ("item1", "item2")
# useful if ou dont want the list to change

# set - unordered unqique items (no duplicates) = {"item1", "item2"}
# useful if you want no duplicates 

# dictionary - key value pairs = {"key" : "value"} keys are unqiue 
# useful to access via key ie. membership number : name 

print("--------------------------------------------------------")
# Loops
print("LOOPS")
print("-----")

group_list = ["Katy", "Kat", "Graham", 
    "Markus", "Ash", "Tom", "Antony",
    "Michal", "Elmi"]

print(group_list)
print("")


# for loop for each_item in 
for eachPerson in group_list:
    print(eachPerson)
print("")

# range - start, stop, distance
for eachInt in range(0, 100, 10):
    print(eachInt)
print("")

# while
an_int = 5
while an_int > 0:
    print(an_int)
    an_int -= 1

print("-----------------------------------------------------")
# ----------------------------------------------------------
import random # should be at top but ive put it here for this exampe

rand_int = random.randint(1, 50)
my_num = 21
count = 1

while rand_int != my_num:
    print(f"Try {count} : {rand_int}")
    count += 1
    rand_int = random.randint(1, 50)
print(f"Try {count} : {rand_int} {my_num}- Matching numbers")
