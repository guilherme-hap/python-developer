print(True and True and True)
print(True and False and True)
print(False and False and False)
print(True or True or True)
print(True or False or False)
print(False or False or False)

balance = 1000
withdrawal = 250
limit = 200
special_account = True

expression = balance >= withdrawal and withdrawal <= limit or special_account and balance >= withdrawal
print(expression)

expression_2 = (balance >= withdrawal and withdrawal <= limit) or (special_account and balance >= withdrawal)
print(expression_2)

conta_normal_com_saldo_suficiente = balance >= withdrawal and withdrawal <= limit
conta_especial_com_saldo_suficiente = special_account and balance >= withdrawal

expression_3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(expression_3)