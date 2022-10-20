def register (pname, age, mclass, hobby, Parentname):
    print(f"my name is {pname} and i am {age} years old and i am in {mclass} and i love {hobby} and the name of my parents is {Parentname}")
    
pname = input("enter your name: ")
age = int(input("enter your age: "))
mclass = input("enter your class: ")
hobby = input("enter your hobby: ")
Parentname = input("enter your parent names: ")

register(pname, age, mclass, hobby, Parentname)