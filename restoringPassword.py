string = str(input())

number0 = str(input())
number1 = str(input())
number2 = str(input())
number3 = str(input())
number4 = str(input())
number5 = str(input())
number6 = str(input())
number7 = str(input())
number8 = str(input())
number9 = str(input())

number = ""
i = 0
while i <= 80:
	try:
		if string[i:i + 10] == number0:
			number += "0"
		elif string[i:i + 10] == number1:
			number += "1"
		elif string[i:i + 10] == number2:
			number += "2"
		elif string[i:i + 10] == number3:
			number += "3"
		elif string[i:i + 10] == number4:
			number += "4"
		elif string[i:i + 10] == number5:
			number += "5"
		elif string[i:i + 10] == number6:
			number += "6"
		elif string[i:i + 10] == number7:
			number += "7"
		elif string[i:i + 10] == number8:
			number += "8"
		elif string[i:i + 10] == number9:
			number += "9"
		
		i += 10
	
	except IndexError:
		pass

print(number)