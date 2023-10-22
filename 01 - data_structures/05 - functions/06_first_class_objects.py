def sum(a, b):
    return a + b


def display_result(a, b, function):
    result = function(a, b)
    print(f"The result of operation {a} + {b} is {result}")


display_result(10, 10, sum)  # The result of operation 10 + 10 is 20