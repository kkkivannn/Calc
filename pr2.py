import calendar
year = int(input("Укажите год: "))
result = 0
for i in range(1, 13):
    day = calendar.monthrange(year, i)[1]
    for j in range(1, day+1):
        firstNumber = int(j/10)
        secondNumber = int(j%10)
        result += firstNumber + secondNumber
print(result)