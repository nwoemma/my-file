def list_numbers (intergers):
    numbers =""
    for i in intergers:
        numbers = i + numbers
    return numbers
intergers = input("enter the numbers: ")
print("the interger is " ,list_numbers(intergers))