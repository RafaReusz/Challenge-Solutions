alcohol = ["ABSINTH", "BEER", "BRANDY", "CHAMPAGNE", "GIN", "RUM", "SAKE", "TEQUILA", "VODKA", "WHISKEY", "WINE"]

n = int(input())
verify = 0
for i in range(n):
	inputDrinkOrAge = str(input())
	if inputDrinkOrAge.isnumeric() == True:
		inputDrinkOrAge = int(inputDrinkOrAge)
		if inputDrinkOrAge < 18:
			verify += 1
	else:
		if inputDrinkOrAge in alcohol:
			verify += 1

print("%d" % (verify))