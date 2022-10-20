def studentform():
    name = input("enter your names: ")
    course = input("enter the course you are doing: ")
    age = int(input("enter your age: "))
    while age < 18:
        return age
        print("you have reached the age to join this institution ")
        t.sleep(1)        
        break
       
    Reg_no = input("enter your registration number: ")
    while "/" not in Reg_no:
        print("please add / to your registration number")
        
        Reg_no = input("enter a valid registration number: ")
    email = input("enter your email: ") 
    while "@" not in email:
        print("@ is not in your email: ")
        print("please add @ to your email: ")
    while ".com" not in email:
        print("this password is invaild, .com is missing")
    
        email = input("enter a valid email: ")
    
    password1 = (input('enter a password: '))
    while len(str(password1)) < 8:
        print('password should be 8 or more charaters ')
        password1 = (input('enter a password: '))
        password2 = (input('reenter password: '))    
    password1 = input("enter a password: ")
    password2 = input("confirmm your password: ")    
    while password1!=password2:
        print({name}, "please the two password didnt match: ")
        print({name}, "please check your password and try again: ")
        password1 = input("enter a password: ")
        password2 = input("confirmm your password: ") 
    parentname = input("enter your parents name: ")
    NameOfKin = input("enter thr name of your sponsor: ")
    Stateoforigin = input("enter your state of origin: ")
    LocalGovernmentArea = input("enter your local government area: ")

    if (True):
        print("please wait a little....")
        t.sleep(2)
        print("the form is almost ready ....")

studentform()