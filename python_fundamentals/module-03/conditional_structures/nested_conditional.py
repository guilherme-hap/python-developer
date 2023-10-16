normal_account = False
college_account = False
special_account = True

balance = 2000
withdrawal = 1500
overdraft = 450

if normal_account:

    if balance >= withdrawal:
        print("Amount successfully withdrawn!")
    elif withdrawal <= (balance + overdraft):
        print("Withdrawal made using the overdraft!")
    else:
        print("Couldn't withdraw, insufficient balance!")

elif college_account:

    if balance >= withdrawal:
        print("Amount successfully withdrawn!")
    else:
        print("Insufficiente balance!")

elif special_account:
    print("Special account selected!")

else:
    print("System did not recognize your account type, please contact your manager.")