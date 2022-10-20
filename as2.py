def calculate(num, num2, num3, num4):
    num1 = int(input("enter a number: "))
    num2 = int(input("enter a number: "))
    num3 = int(input('enter a number: '))
    num4 = int(input("enter a number: "))
    t_num = (num1,num2,num3,num4)

    print(max(t_num))
    print(min(t_num))
calculate(1,2,3,4)