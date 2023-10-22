balance = 2000
withdrawal = 2500

status = "Success" if balance >= withdrawal else "Failure"

print(f"{status} to withdraw!")