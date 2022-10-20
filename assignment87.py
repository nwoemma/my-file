def bank_services():
    import time as t
    firstname = input("enter your first name: ")
    lastname = input("enter your last name: ")
    age = int(input("enter your age: "))
    while age < 18:
        print("age not reached to have transaction in this bank....")
        age = int(input("enter your age: "))

    user_pin = int(input("enter your pin number: "))

    while len(str(user_pin)) != 4:
        print("pin must be 4-digit ")
        user_pin = int(input("enter your 4 digit number: "))
        user_pin2 = int(input("re-enter your 4 digit number: "))

    user_pin2 = int(input("re-enter your 4 digit numbers: "))

    while user_pin != user_pin2:
        print("pin not matched")

        user_pin = int(input("enter your 4 digit number: "))
        user_pin2 = int(input("re-enter your 4 digit number: "))

    user_pin2 = int(input("re-enter your pin number: "))

    user_balance = 5000
    input_pin = int(input("enter your pin number: "))
    while input_pin != user_pin:
        print("pin not matched ")

        input_pin = int(input("enter the correct pin: "))
    if(True):
        print("\t\t0.Logout and exit")
        print("\t\t1.View Account balance")
        print("\t\t2.Withdraw Money")
        print("\t\t3.Deposit card")
        print("\t\t4.Change PIN")
        print("\t\t5.Return card") 
        choice = int(input("enter a number to continue \n "))
        if choice == 0:
            print(f"Exiting... ")
            t.sleep(2) 
            print(f"{firstname} you have been logged out \n\n ")

        elif choice in (1,2,3,4,5):
            numoftries = 3
            while (numoftries != 0):
                input_pin =int(input("Please enter your 4-digit Pin>> "))
        
                if input_pin == user_pin:
                    print("Account Authorised!\n\n ")
                if choice == 1:
                    print("loading accoumt balance.... ")
                    t.sleep(1.3)
                    print(f"{firstname}, your account Balance is Rs ", user_balance)
                    break
                elif choice == 2: 
                    print("Opening Cash Withdrawal... ")
                    t.sleep(1.3)
                while (True):
                    Withdrawal_amt = float(input("enter the amount you want to withdraw >>"))
                    if Withdrawal_amt > user_balance:
                        print("Can't withdraw Rs", Withdrawal_amt)
                        print("please enter a lower ammount")
                        continue
                    else:
                        print("Withdrawing Rs", Withdrawal_amt)
                        confirm = input("Confirm? Yes/No >" )
                    if confirm in ('Yes' , 'yes'):
                        user_balance-= Withdrawal_amt
                        print("Ammount withdrawn - Rs.", Withdrawal_amt)
                        print("Remaining balance - Rs.", user_balance, end = "\n\n")
                    else:
                        print("Cancelling transaction...")
                        t.sleep(1.2)
                        print("Transaction Cancelled!\n\n ")

                    break
                elif choice == 3:
                        print("Loading Cash Deposit... ")
                        t.sleep(1.0)
                        
                        Deposit_amt =float(input("Enter the ammount you want to deposit>> "))
                        print("Depositing Rs:", Deposit_amt)
                        confirm = input("Confirm? Yes/No>")
                        if confirm in ('Yes', 'yes' ):
                    user_balance-=Deposit_amt
                    print("Ammount deposited - Rs.", Deposit_amt)
                    print("Remaining balance - Rs.", user_balance, end ="\n\n")
                else:
                    print("Cancelling transaction...")
                    t.sleep(1.2)
                    print("Transaction Cancelled!\n\n ")

                break

            elif choice == 4:
                print("Changing PIN")
                t.sleep(1.0)

                new_pin = int(input("Enter your new PIN>> "))

                print("Changing PIN to ", new_pin)
                confirm = input("Confirm? Yes or No >")
                if confirm in ('Yes','yes'):
                    user_pin = new_pin
                    print("PIN Changed sucessfully!\n\n")
                else:
                    print("Cancelling PIN change... ")
                    t.sleep(1.0)                
                    print("Process Cancelled!\n\n ")

                break
            else:
                print("Loading Card Return...")
                t.sleep (1.5)
                print("Returning your ATM Card")
                confirm = input("Confirm? Yes or No >>")
                if confirm in ('Yes', 'yes'):
                    print("Card returned successful! \n\n")
                else:
                    print("Cancelling PIN change... ")
                    t.sleep(1.0)                
                    print("Process Cancelled!\n\n ")

            break    
                
        else:
            numoftries -= 1
            print(f"{firstname},Pin is incorrect! Number of tries left -", numoftries, end ="\n\n")

    else:
        print("Invalid input!")
        print("\t\t0. Enter 0 to Logout and Exit! ")
        pass
bank()