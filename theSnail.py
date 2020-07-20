while True:
	H, U, D, F = input().split()
	H = int(H)
	U = int(U)
	D = int(D)
	F = int(F)

	if H == 0:
		break

	else:
		reached = False
		day = 1
		fatigueFactor = (F / 100) * U
		initialDistance = 0

		while H > initialDistance and initialDistance >= 0 and U >= 0:
			initialDistance += U
			U -= fatigueFactor

			if initialDistance > H:
				reached = True
				# breaking the loop
				initialDistance = H + D + 1
					
			initialDistance -= D
			if initialDistance <= H and initialDistance >= 0:
				day += 1

		if U < 0:
			while initialDistance > 0:
				initialDistance -= D
				if initialDistance >= 0:
					day += 1
		
		
		
		if reached == True:
			print('success on day %d' % (day))
		
		else:
			print('failure on day %d' % (day))