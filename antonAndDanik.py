n = int(input())
s = str(input())

antonWins = 0
danikWins = 0
for i in range(n):
	if s[i] == 'A':
		antonWins += 1
	elif s[i] == 'D':
		danikWins += 1

if antonWins > danikWins:
	print('Anton')

elif antonWins < danikWins:
	print('Danik')

else:
	print('Friendship')