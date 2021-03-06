# Lists
# -----------------------------------------------------------------------------------------------------------------------
# Lists are MUTABLE
# Syntax [""]
# CRUD: CREATE READ UPDATE AND DELETE

# Let's create a shopping list

shopping_list = ["Juice", "Strawberries", "Yoghurt", "Chicken", "Raspberries", "Butter"]
                  0           1             2          3            4            5
print(shopping_list)
print(type(shopping_list))
print(shopping_list[2])
print(shopping_list[4])
print(shopping_list[1])

# If we need to replace something from the list

shopping_list[5] = "Oats"
print(shopping_list)

# If we need to add something

shopping_list.append("Mangoes")
print(shopping_list) # notice that it adds it add the end of the list

# If we need to remove from our shopping list, we have a method called remove

shopping_list.remove("Oats")
print(shopping_list)

shopping_list.pop() # removed the last item from the list
print(shopping_list)


# Tuples
# ----------------------------------------------------------------------------------------------------------------------
# Tuples are IMMUTABLE
#
# Why do we need tuples? What sort of data types never change?
# - Something we don't want the user to change
# - For example like DOB, Date of Birth, Date of Death

essentials = ("Eggs", "Milk", "Bread")
#               0       1        2
print(essentials)
print(type(essentials))
print(essentials[1])

# try replacing Bread with Yoghurt and see what happens
essentials[2] = "Yoghurt" # the output will show a TypeError as tuples are immutable
