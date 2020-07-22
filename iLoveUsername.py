n = int(input())
arrayContests = input().split()

for i in range(n):
	arrayContests[i] = int(arrayContests[i])

amazing = 0
minPoints = arrayContests[0]
maxPoints = arrayContests[0]

for i in range(1, n):
	if arrayContests[i] > maxPoints:
		amazing += 1
		maxPoints = arrayContests[i]
	
	elif arrayContests[i] < minPoints:
		amazing += 1
		minPoints = arrayContests[i]

print("%d" % (amazing))