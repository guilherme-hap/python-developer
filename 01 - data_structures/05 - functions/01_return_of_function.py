def calc_total(numbers):
    return sum(numbers)


def return_previous_and_next(number):
    previous = number - 1
    next = number + 1

    return previous, next


print(calc_total([10, 20, 34]))  # 64
print(return_previous_and_next(10))  # (9, 11)