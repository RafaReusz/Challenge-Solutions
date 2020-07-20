n = int(input())

parameter = 0
while n != parameter:
	if parameter % 2 == 0:
		print("I hate", end=" ")
	else:
		print("I love", end=" ")
	
	if parameter + 1 == n:
		print("it")
	else:
		print("that", end=" ")
	
	parameter += 1