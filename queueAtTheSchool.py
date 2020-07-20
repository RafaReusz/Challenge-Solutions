n, t = input().split()
n = int(n)
t = int(t)

inputLetters = str(input())
arrayQueue = []
for j in range(n):
	arrayQueue.append(inputLetters[j])

while t != 0:
	i = 0
	while i < len(arrayQueue):
		if (i != len(arrayQueue) - 1) and (arrayQueue[i] == 'B' and arrayQueue[i + 1] == 'G'):
			arrayQueue[i] = 'G'
			arrayQueue[i + 1] = 'B'
			i += 2
		else:
			i += 1
	t -= 1

for j in range(n):
	if j + 1 == n:
		print(arrayQueue[-1])
	else:
		print(arrayQueue[j], end='')