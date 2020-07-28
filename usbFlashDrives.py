n = int(input())

arrayDrives = []

m = int(input())

for i in range(n):
	ai = int(input())
	arrayDrives.append(ai)

numberOfDrives = 0
totalSpace = 0
while totalSpace < m:
	numberOfDrives += 1
	totalSpace += max(arrayDrives)
	arrayDrives.remove(max(arrayDrives))

print("%d" % (numberOfDrives))
