class product_and_price():
    def goods(self):
        total = price*quantity
        print(f'product name: {name}, product price: {price}, product quantity {quantity}, total {total}')

name = int(input("""
1. laptop = 350000.00
2. iphone X = 344000.00
3. infinix smart 5 = 45000.00
Which one do you want to buy? 
"""))
quantity = int(input('Enter the quantity '))
if name == 1:
    price = 350000
    total = 350000*quantity
    print('laptop', 350000, quantity, total)

if name == 2:
    price = 344000
    total = 344000*quantity
    print('iphone X', 344000, quantity, total)
    
if name == 3:
    price = 45000
    total = 45000*quantity
    print('infinix', 45000, quantity,total)

b = product_and_price()
b.goods()