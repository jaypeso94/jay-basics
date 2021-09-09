listA = [2, 0, 1, 3, 7, 4, 6, 9, 8]
listB = [19, 12, 76, 43, 23, 15, 54, 28]

def listAB(listA, listB):
	listA.sort()
	listB.sort()

	listC = (listA, listB)
	return listC

listABC = listAB(listA, listB)
print(listABC)	

#Not sure if numbers were meant to be included but
#I figured you were looking to start with something simple
