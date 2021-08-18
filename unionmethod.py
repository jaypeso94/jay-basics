#Assignment #2, Sets, sorting a list of them to start.

# In order to sort a set I have to convert the unorder list into a function. Otherwise Ill keep getting a syntax error 

set_1 = {"message", "tag", "framework"}
all_set1 = set(set_1)
set_2 = {"message", "metadata", "token"}
all_set2 = set(set_2)
set_3 = {"metadata", "tag", "token"}
all_set3 = set(set_3)
# Need to understand the definition of symmetric/difference
all_setX = set(set_1).symmetric_difference(set(set_2))
all_setY = set(set_2).symmetric_difference(set(set_3))


# Taking notes online/stackoverflow I can try one of the methods. Here I tried the union method but could only do so between two sets.
list_of_sets = all_setX.union(all_setY)

print(list_of_sets)










