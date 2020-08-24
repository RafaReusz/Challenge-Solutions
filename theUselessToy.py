begin, end = input().split()
begin = str(begin)
end = str(end)

n = int(input())


arrayPosicoes = ["^", ">", "v", "<"]
finalPosition = n % 4

verifyClockWise = False
verifyCounterClock = False

parameter = arrayPosicoes.index(begin)

#clockWise
while finalPosition != 0:
	if parameter != 3:
		parameter += 1
	else:
		parameter = 0
	finalPosition -= 1


if arrayPosicoes[parameter] == end:
	verifyClockWise = True


finalPosition2 = n % 4
parameter2 = arrayPosicoes.index(begin)
while finalPosition2 != 0:
	if parameter2 != 0:
		parameter2 -= 1
	else:
		parameter2 = 3
	finalPosition2 -= 1

if arrayPosicoes[parameter2] == end:
	verifyCounterClock = True



if verifyClockWise == True and verifyCounterClock == False:
	print("cw")
elif verifyClockWise == False and verifyCounterClock == True:
	print("ccw")
else:
	print("undefined")