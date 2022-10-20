def goods(name, price,quantity,total):
    total = price*quantity
    print(f'product name: {name}, product price: {price}, product quantity {quantity}, total {total}')

name = int(input("""
1. laptop = 350000
2. iphone X = 344000
3. infinix smart 5 = 45000
Which one do you want to buy? 
"""))
quantity = int(input('Enter the quantity '))
if name == 1:
    total = 350000*quantity
    goods('laptop', 350000, quantity,total)

if name == 2:
    total = 344000*quantity
    goods('iphone X', 344000, quantity,total)
    

if name == 3:
    total = 45000*quantity
    goods('infinix', 45000, quantity,total)