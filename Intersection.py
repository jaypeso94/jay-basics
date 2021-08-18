set_1 = {"message", "tag", "framework"}
set1 = set(set_1)
set_2 = {"message", "metadata", "token"}
set2 = set(set_2)
set_3 = {"metadata", "tag", "token"}
set3 = set(set_3)

set_X = set1.intersection(set2, set3)
# The message "set()" is recieved


set_Y = set2.intersection(set3)

print(set_X)
print(set_Y)

#Unable to find intersection between the three sets
#There is not any shared values that connect all three sets
