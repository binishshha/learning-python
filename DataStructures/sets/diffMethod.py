#--------- DIFFERENCE -----------------
class1 = {'ram', 'sam', 'hari'}
class2 = {'sita', 'gita', 'hari'}

# difference() returns a new set and does not change original sets
diff = class1.difference(class2)
print(f"class1 = {class1}")
print(f"class2 = {class2}")
print(f"difference = {diff}")

# using - operator
diff_op = class1 - class2
print(f"difference using operator = {diff_op}")
print(f"class1 = {class1}")
print(f"class2 = {class2}")

# difference_update() modifies class1
class1.difference_update(class2)
print(f"after difference_update:")
print(f"class1 = {class1}")
print(f"class2 = {class2}")


#--------- SYMMETRIC DIFFERENCE -----------------
class1 = {'ram', 'sam', 'hari'}
class2 = {'sita', 'gita', 'hari'}

# symmetric_difference() returns new set with uncommon elements from both
sym_diff = class1.symmetric_difference(class2)
print(f"class1 = {class1}")
print(f"class2 = {class2}")
print(f"symmetric difference = {sym_diff}")

# using ^ operator
sym_diff_op = class1 ^ class2
print(f"symmetric difference using operator = {sym_diff_op}")
print(f"class1 = {class1}")
print(f"class2 = {class2}")

# symmetric_difference_update() modifies class1
class1.symmetric_difference_update(class2)
print(f"after symmetric_difference_update:")
print(f"class1 = {class1}")
print(f"class2 = {class2}")
