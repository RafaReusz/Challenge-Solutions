n = str(input())
count = 0
for i in range(len(n)):
	if n[i] == '4' or n[i] == '7':
		count += 1

nearlyLucky = True
stringCount = str(count)
for j in range(len(stringCount)):
	if stringCount[j] != '4' and stringCount[j] != '7':
		nearlyLucky = False
		break

if nearlyLucky:
	print('YES')
else:
	print('NO')