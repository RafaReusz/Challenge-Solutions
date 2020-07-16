def verifyVowel(x):
	if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
		return True
	else:
		return False

n = int(input())
for _ in range(n):
	firstString = str(input())
	secondString = str(input())
	
	if (len(firstString) == len(secondString)):

		parameter = True

		for i in range(len(firstString)):
			if (firstString[i] != secondString[i]) and (verifyVowel(firstString[i]) == False or verifyVowel(secondString[i]) == False):
				parameter = False
		
		if parameter == True:
			print('Yes')
		
		else:
			print('No')		


	else:
		print('No')