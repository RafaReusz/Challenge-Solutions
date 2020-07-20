word = str(input())

upperLetters = 0
lowerLetters = 0

for i in range(len(word)):
	if word[i].islower():
		lowerLetters += 1
	else:
		upperLetters += 1

if upperLetters > lowerLetters:
	print(word.upper())
else:
	print(word.lower())