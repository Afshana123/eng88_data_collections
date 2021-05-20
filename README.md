# Python Data Collections 

- Lists
- Dictionary
- Tuples
- Sets

The difference between a List and a Tuple is that Lists are mutable and Tuples are immutable (you cannot change or update them)

## Lists 


```python
# Lists
# Syntax [""]
# CRUD: CREATE READ UPDATE AND DELETE

# Let's create a shopping list

shopping_list = ["Juice", "Strawberries", "Yoghurt", "Chicken", "Raspberries", "Butter"]
#                   0           1             2          3            4            5
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
print(shopping_list)

# If we need to remove from our shopping list, we have a method called remove

shopping_list.remove("Oats")
print(shopping_list)

shopping_list.pop() # removed the last item from the list
print(shopping_list)

```

## Tuples 

```python
# Tuples are IMMUTABLE

# Why do we need tuples? What sort of data types never change?
# Something we don't want the user to change
# Something like DOB, Date of Birth, Date of Death

essentials = ("Eggs", "Milk", "Bread")
#               0       1        2
print(essentials)
print(type(essentials))

# replace bread with Yoghurt
essentials(2) = "Yoghurt"
```

## Dictionaries 

```python
# What are dictionaries?
# They are structured as KEY = VALUE
# VALUE could be string, int, list
# Syntax {}

student_1 = {
    "Name" : "Afshana",
#   "Key"  : "Value"
    "Stream" : "Cyber Security",
    "Completed_Lessons" : 3,
    "Complete_Lessons" : ["Variables", "Operators", "Data_Collections"] # List
}

print(student_1)
# We can fetch the values with the keys
print(student_1["Name"])
print(student_1["Stream"])
print(student_1["Complete_Lessons"])

# Display only 'OPERATORS' FROM THE LIST INSIDE DICTIONARY
print(student_1["Complete_Lessons"][1])

# You can print all the keys as follows
print(student_1.keys())

# You can print all the values as follows
print(student_1.values())
```

## Sets 

```python
# Sets are data collection but different is that they are unordered
# Syntax name = {}
# You can use sets if you are not worried about the organisation or order of how it is stored

car_parts = {"Wheels", "Doors", "Engine"}

print(car_parts) # the output is that they elements are printed in a random order everytime it is run. It won't be necessarily in the order you have assigned them.


# To add an element
car_parts.add("Windows")
print(car_parts)

# To remove an element
car_parts.discard(("Doors"))
print(car_parts)

# Frozen sets are like Tuples (immutable)
frozen_set = ([1,2,3,4])
print(frozen_set)
```
