n = int(input("Enter the number of celsius termperatures to display: "))

print("Celsius  Fahrenheit\n")
fahrenheit = 0

for celcius in range(n):
	fahrenheit = 9 / 5 * celcius + 32
	print(celcius, "     ", fahrenheit)
