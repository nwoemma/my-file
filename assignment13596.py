def studentform(firstname, lastname, age, password1, password2, Reg_no, Stateoforigin, Parentname, NameOfKin, email):
    print(f'my name is {firstname}, my surname is {lastname}, i am {age}, my password is {password1}, and to confirm my password you use {password2}, my registration number is {Reg_no}, amd my state of origin is {Stateoforigin},  my parents name are {Parentname}, the people spopnsing me is {NameOfKin} and my email is {email}')    
import time as t
firstname = input("enter your first name: ")
lastname = input("enter your surname: ")
age = int(input("enter your age: "))
while age < 18:
    t.sleep(1)
    break
    print("you have reached the age to join this institution ")
password1 = (input('enter a password: '))
while len(str(password1)) !=8:
 print('password should be 8 charaters ')
 password1 = (input('enter a password: '))
 password2 = (input('reenter password: '))

password2 = (input('reenter password: '))

while password1 !=password2:
    print('password not matched')
        
    password1 = (input('enter a password: '))
    password2 = (input('reenter password: '))
Reg_no = input("enter your registration number: ")
while ("clu/20") not in Reg_no:
    print("The registration number is invalid... ")
    print("please enter a valid registration number: ")

    Reg_no = input("enter your registration number: ")
Stateoforigin =input("enter your state of origin: ")
Parentname = input("enter the name of your parent: ")
NameOfKin = input("enter the name of your kin: ")
email = input("enter your email: ")
while "@" not in  email:
    print("this password is invaild , @ is missing")
    
    email = input("enter a valid email: ")
while ".com" not in email:
    print("this password is invaild, .com is missing")
    
    email = input("enter a valid email: ")
        
    if (True):
        print("please wait a little....")
        t.sleep(2)
        print("the form is almost ready ....")
        pass

studentform(firstname,lastname,age,password1,password2,Reg_no,Stateoforigin,Parentname,NameOfKin,email)
