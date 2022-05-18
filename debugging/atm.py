def atm(language,bank_name):
    if language=="english":
        print("welcome to", bank_name)
        balance=10000
        print("choose transaction","\n", "1.Balance Enquiry","\n", "2.Withdrawal","\n","3.Deposit","\n","4.transfer","\n","5.Exit")
        transaction=int(input("enter the transaction"))
        if transaction==1 or 2 or 3 or 4 or 5:
            secret_pin=int(input("enter the secret pin"))
            saved_pin=2222
            if secret_pin==saved_pin:
                print("correct pin")
                if transaction==1:
                    print("your balance is", balance)
                    print("thank you, collect your card")
                elif transaction==2:
                    withdrawal=int(input("enter the withdrawal amount"))
                    if withdrawal<=balance:
                        print("remaining balance is", balance-withdrawal)
                        print("thank you, collect your card")
                    else:
                        print("insufficient balance")
                elif transaction==3:
                    deposit=int(input("enter the deposit amount"))
                    if deposit>=1:
                        print("balance is", balance+deposit)
                        print("thank you, collect your card")
                    else:
                        print("deposit fail")
                elif transaction==4:
                    transfer_amount=int(input("enter transfer amount"))
                    if transfer_amount<=balance:
                        print("balance is",balance-transfer_amount)
                        print("transfer successfull","\n","thank you, collect your card")
                    else:
                        print("insufficient balance for transfer")
                elif transaction==5:
                    exit=input("are you sure you want to exit")
                    if exit=="yes":
                        print("thank you for visiting")
                    else:
                        print("choose transaction","\n","1.bal.enq","\n","2.withdraw","\n","3.deposit","\n","4.transfer","\n" " 5.exit")
                else:
                    print("transaction code not found")
            else:
                print("incorrect pin")
        else:
            print("error")
    else:
        print("language not available")
language=input("enter the language:")
bank_name=input("enter bank name:")
atm(language,bank_name)