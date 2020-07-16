import math

while True:

	a, b, s, m, n = input().split()
	a = int(a)
	b = int(b)
	s = int(s)
	m = int(m)
	n = int(n)
	if a == 0 and b == 0 and s == 0 and m == 0 and n == 0:
		break

	else:
		# corrigir
		distanceX = (a * m)
		distanceY = (b * n)

		velInX = (distanceX / s)
		velInY = (distanceY / s)

		velTotal = ((velInX ** 2) + (velInY ** 2)) ** 0.5

		angleRadians = math.atan(velInY / velInX)
		angleDegrees = math.degrees(angleRadians)

		print("%.2f %.2f" % (angleDegrees, velTotal))