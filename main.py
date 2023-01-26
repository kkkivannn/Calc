while(True):
    operation = input("Введите операцию: ")
    if operation == '0':
        print("Спасибо, пожалуйста.")
        break
    count_num = int(input("Введите кол-во чисел: "))
    index = 0
    for index in range(count_num):
        if operation == "+":
            if index == 0:
                num = int(input(f"{index+1}: "))
                result = num
            else:
                result += int(input(f"{index+1}: "))        
        elif operation == "-":
            if index == 0:
                num = int(input(f"{index+1}: "))
                result = num
            else:
                result -= int(input(f"{index+1}: "))
        elif operation == "*":
            if index == 0:
                num = int(input(f"{index+1}: "))
                result = num
            else:
                result *= int(input(f"{index+1}: "))
        elif operation == "/":
            if index == 0:
                num = int(input(f"{index+1}: "))
                result = num
            else:
                num = int(input(f"{index+1}: "))
                if num == 0: 
                    print("Делить на ноль нельзя")
                    break
                else:
                    result = result / num
        
    
    print(result)