num1, num2 = map(int, input().split(" "))

if num1 > num2:
	print(num1 - num2 - 1)
	for x in range(num2 + 1, num1):
		print(x, end=" ")
elif num1 < num2:
	print(num2 - num1 - 1)
	for x in range(num1 + 1, num2):
		print(x, end=" ")
else:
	print(num1 - num2)