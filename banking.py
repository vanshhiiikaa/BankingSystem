account = {
    82149 : {
        "name" : "Ally",
        "age" : 28,
        "phone number" : 9045310829,
        "PIN" : 1234,
        "Balance" : 10000,
        "Transactions": []
          },
    
    78429 : {
        "name" : "Sicly",
        "age" : 34,
        "phone number" : 92781263168,
        "PIN" : 5678,
        "Balance" : 20000,
        "Transactions": []
          }
    }

account_num = int(input("Enter your account number: "))
pin = int(input("Enter PIN: "))

if account_num in account:
    if account[account_num]["PIN"] == pin:
        print("Login successful")
        print("Welcome",account[account_num]["name"])
        print("Your balance is Rs.",account[account_num]["Balance"])


    while True:

        print("BANK MENU\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Transactions\n5. Log out")

        menu = int(input("Enter key for for following operations"))
        
        if menu == 1:
            print("Your balance is Rs.",account[account_num]["Balance"])

        elif menu == 2:
            deposit = int(input("Enter amount you want to deposit:"))
            if deposit <= 0:
                print("Amount must be greater than Rs. 0")
            else:
                account[account_num]["Balance"] += deposit
                account[account_num]["Transactions"].append(f"Deposited Rs. {deposit}")
                print("Deposited: Rs.",deposit)
                print("New Balance: Rs.",account[account_num]["Balance"])

        elif menu == 3:
            withdraw = int(input("Enter amount you want to withdraw:"))
    
            if withdraw > account[account_num]["Balance"]:
                print("Insufficient balance")
                print("Available Balance Rs.", account[account_num]["Balance"])

            else:
                account[account_num]["Balance"] -= withdraw
                account[account_num]["Transactions"].append(f"Withdrawn Rs. {withdraw}")
                print("Withdrawn: Rs.", withdraw)
                print("New Balance: Rs.", account[account_num]["Balance"])

        elif menu == 4:
            print("Transaction History")
    
            if len(account[account_num]["Transactions"]) == 0:
                print("No transactions found.")
            else:
                for transaction in account[account_num]["Transactions"]:
                    print(transaction)

        elif menu == 5:
            print("Logged out successfully")
            break

    else:
        print("Wrong PIN")

else:
    print("Account does not exist")