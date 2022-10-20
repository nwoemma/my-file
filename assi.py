def numbers(int):
    num = int((input("enter the number: ")))
    count = int(input("enter the number count: "))
    print("the multiplication table of number of", num, "is")
    if count in range(1,140):
        print (num, 'x', count, '=', num * count)
numbers(int)