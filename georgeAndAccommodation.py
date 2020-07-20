n = int(input())

roomsAvailable = 0

for i in range(n):
	p, q = input().split()
	p = int(p)
	q = int(q)

	if q - p >= 2:
		roomsAvailable += 1

print("%d" % (roomsAvailable))