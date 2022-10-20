def calculate(name,product, price, quantity ):
     print(f"dear {name}, you are wwelcome to EmyConInterprice.com...   ")
     print("""
    Here are the product and there prices
    1. shirts = 3500
    2. shoes = 4000 
    3. troswers = 3500
  """)

     product = int(input("enter the product the customer want to purchase: "))
     price = int(input("enter the price of the product:"))
     if product == 1:
          quantity = int(input("how many shirts do the customer want to buy: "))
          print(f"total ammount is", {price * quantity})
     if product == 2:
          quantity = int(input("how many shoes do the customer want to buy: "))
          print(f"total ammount is", {price * quantity})
     if product == 3:
          quantity = int(input("how many troswers do the customer want to buy: ")) 
          print(f"total ammount is",  {price * quantity})     
calculate ('emeka','shirt', 3500, 4)
