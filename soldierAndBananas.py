k, n, w = input().split()
k = int(k)
n = int(n)
w = int(w)

dollarsHave = n
costFirst = k
howMany = w

lastCost = k + (w - 1) * k
total = ((k + lastCost) * w) / 2

if dollarsHave >= total:
	print(0)
else:
	print("%d" % (total - dollarsHave))