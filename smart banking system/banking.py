data={}
print("--------WELCOME TO HDMI BANK--------")
while True:
    print("1.Create Account")
    print("2.Login")
    print("3.Exit")
    choice=input("Enter your choice(1-3): ")
    if choice=="1":
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        ini_money = int(input("Enter your initial money: ₹"))
        import random
        acc_num = random.randrange(pow(10, 3), pow(10, 5))
        data[acc_num]={"name":name,"password":password,"initial money": ini_money}
        more = input("Want to add more accounts? (y/n): ")
        if more.lower() == "y":
            print(data)
            print("Accounts created.")
            continue
        else:
            print(data)
            print("Accounts created.")
            continue
    elif choice=="2":
        acct_num=int(input("Enter your account number: "))
        password=input("Enter your password: ")
        if acct_num in data:
            acct = data[acct_num]
            passcode = acct["password"]
            if password==passcode:
                print("Login Successful.")
            else:
                print("*****Password is wrong*****.")
                continue
        else:
            print("This account number does not exists.")
            continue
        while True:
            print("1.Check Balance")
            print("2.Deposit")
            print("3.Withdraw")
            print("4.Transfer")
            print("5.Logout")
            choice=input("Enter your choice(1-5): ")
            acct = data[acct_num]
            if choice=="1":
                print(f"Your current balance is:₹{acct["initial money"]}")
            elif choice=="2":
                deposit=int(input("Enter the amount to be deposited: "))
                acct["initial money"]+=deposit
                print(f"The new balance is: ₹{acct["initial money"]}")
            elif choice=="3":
                withdraw=int(input("Enter the amount to be withdrawn: "))
                if withdraw<0:
                    print("You entered the negative amount.")
                    continue
                elif withdraw>acct["initial money"]:
                    print("You don't have that much money in our account. TRY AGAIN!")
                    continue
                else:
                    acct["initial money"]-=withdraw
                    print(f"Your balance is ₹{acct["initial money"]}")
            elif choice=="4":
                receiver_acct=int(input("Enter the receiver account number: "))
                if receiver_acct in data:
                    account = data[receiver_acct]
                    print("This account exist.")
                else:
                    print("This account number does not exist.")
                    continue
                send_amount=int(input("Enter the amount to be sent: ₹"))
                if send_amount>acct["initial money"]:
                    print(f"You don't have enough money.You have only ₹{acct["initial money"]}")
                    continue
                else:
                    acct["initial money"]-=send_amount
                    print(f"Now your current balance is₹{acct["initial money"]}")
                    account["initial money"]+=send_amount
            elif choice=="5":
                print("You have been logged out!")
                break
            else:
                print("Invalid choice")
                continue
    elif choice=="3":
        print("Thanks for the time!")
        break
    else:
        print("****Invalid Choice****")
        continue


