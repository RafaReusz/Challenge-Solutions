n, k = input().split()
n = int(n)
k = int(k)

while k != 0:
	string_n = str(int(n))
	if string_n[-1] == '0':
		n /= 10
	else:
		n -= 1
	k -= 1

print("%d" % (n))