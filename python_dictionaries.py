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

