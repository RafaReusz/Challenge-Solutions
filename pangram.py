n = int(input())
string = (str(input()).lower())

pangram = True
for i in range(97, 123):
	if chr(i) not in string:
		pangram = False

if pangram:
	print("YES")
else:
	print("NO")