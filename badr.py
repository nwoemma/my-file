# x = input("enter a number")
# y = input("enter a number")
# for i in int:
#     i = x + y
# print(i)

pin1 = int(input('enter a pin: '))
while len(str(pin1)) !=4:
    print('pin must be 4 digit')
    pin1 = int(input('enter a pin: '))
    pin2 = int(input('reenter pin: '))

pin2 = int(input('reenter pin: '))

while pin1 !=pin2:
    print('pin not matched')
        
    pin1 = int(input('enter a pin: '))
    pin2 = int(input('reenter pin: '))




