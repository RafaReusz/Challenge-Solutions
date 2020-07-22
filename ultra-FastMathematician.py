input1 = str(input())
input2 = str(input())

answer = ""
for i in range(len(input1)):
	if input1[i] != input2[i]:
		answer += "1"
	else:
		answer += "0"

print(answer)