def reverse(x):
	return x[::-1]

s = str(input())
t = str(input())

if (reverse(s) == t):
	print('YES')
else:
	print('NO')