def get_num(num):
    sum = 0
    for i in range(1, num+1):
        for j in str(i):
            sum += int(j)
            
    return sum
    
year = int(input("Введите год: "))
answer = 0
if year%4==0 and year%100!=0 or     year%400==0:
         answer += get_num(31)
         answer += get_num(31)
         answer += get_num(31)
         answer += get_num(31)
         answer += get_num(31)
         answer += get_num(31)
         answer += get_num(31)
         answer += get_num(30)
         answer += get_num(30)
         answer += get_num(30)
         answer += get_num(30)
         answer += get_num(29)
else:
         answer += get_num(31)
         answer += get_num(31)
         answer += get_num(31)
         answer += get_num(31)
         answer += get_num(31)
         answer += get_num(31)
         answer += get_num(31)
         answer += get_num(30)
         answer += get_num(30)
         answer += get_num(30)
         answer += get_num(30)
         answer += get_num(28)
         
print(answer)
 