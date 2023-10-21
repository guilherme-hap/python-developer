salary = 2000

def bonus_salary(bonus):
    global salary
    salary += bonus
    return salary

result = bonus_salary(500)  # 2500
print(result)