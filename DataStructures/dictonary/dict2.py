dict1={
    "a":1,
    "b":2,
    "c":3
}
dict2={
    "g":4,
    "a":9,
    "b":8,
    "d":6,
    "c":5,
    "f":2
}

print(f"dict1:{dict1}")
print(f"dict2:{dict2}")
#no new dictonary can be created using update
#.update() method modifies and adds existing keys
#it preserves the order of the dictonary that is to be updated i.e. dictonary order is preserved
#  duplicate keys are updated with value of the new keys
dict1.update(dict2)
print(f"dict1 after updating:{dict1}")

#so we use unpacking method to merge two dictonaries
#---------unpacking method----------
#order follows the unpacking sequence i.e. first dict1 and then dict2
#for duplicate keys too, the values are updated from the dictonary last unpacked
merged_dict={**dict1,**dict2}
print(f"merged dictonary: {merged_dict}")