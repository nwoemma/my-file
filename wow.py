name  = input("enter your name: ")
age = int(input ("enter your age: "))
while age < 18:
     continue
     print("age not reached to have transaction in this organisation")
     age = int(input("enter your age: "))
     print(f"dear {name}, you are wwelcome to EmyConInterprice.com...   ")
     print("""
    Here are the product and there prices
    1. shirts = 3500
    2. shoes = 4000 
    3. troswers = 3500
    """)
_product = int(input ("which product do you want to purchase:\n 1. shirts = 3500\n 2. shoes = 4000\n 3. troswers = 3500\n  "))
if _product == 1:
     quantity = int(input("how many shirts do want to buy: "))
     print(f"total ammount is", {3500 * quantity})
if _product == 2:
     quantity = int(input("how many shoes do want to buy: "))
     print(f"total ammount is", {4000 * quantity})
if _product== 3:
      quantity = int(input("how many troswers do want to buy: ")) 
      print(f"total ammount is",  {3500 * quantity})     

