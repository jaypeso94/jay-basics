#Goal is to create a couple sets
#Sort them within themselves/outside as well alphabetically
Electronics = {"Television", "Computer", "Gamepad"}
Furniture = {"Table", "Chair", "Sofa", "Desk"}
Dishes = {"Plates", "Spoon", "Fork", "Knive", "Pans"}

def Junk(Electronics, Furniture, Dishes):
	GarageSaleA = set(Electronics).symmetric_difference(set(Furniture))
	GarageSaleB = set(Furniture).symmetric_difference(set(Dishes))

	GarageSaleC = GarageSaleA.union(GarageSaleB)

	List_of_Junk = list(GarageSaleC)
	List_of_Junk.sort()
	return List_of_Junk

Junk_to_print = Junk(Electronics, Furniture, Dishes)
print(Junk_to_print)

#Return being used in python helps close/exit the function
#Then continues the main program being run


