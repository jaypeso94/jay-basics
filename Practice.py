#Comparing List


box1 = [ 'Mango', 'Peach', 'Apple', 'Orange', 'Strawberry' ]
#           0         1       2         3           4


# Write an algorithm to sort any array of strings using temp variables


box1 = ['Mango', 'Peach', 'Apple', 'Orange', 'Strawberry']

for ele in sorted(box1):
	print(ele)


box2 = ['red', 'blue', 'purple', 'yellow', 'orange', 'white', 'brown', ]

for ele in sorted(box2):
	print(ele)



lst = [5,6,0,1,2,4,3,9,8,7]

for j in range(0,len(lst)):
	check_for_swap = False
	for i in range(0,len(lst)- 1):
		if lst[i] > lst[i + 1]:
			swap = lst[i]
			lst[i] = lst[i + 1]
			lst[i + 1] = swap
			check_for_swap = True
		if check_for_swap == True:
			break

print(j,lst)