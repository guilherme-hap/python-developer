while True:
    number = int(input("Enter a number: "))

    if number == 10:
        break

    if number % 2 == 0:
        continue

    print(number)


# for number in range(100):

#     if number % 2 == 0:
#         continue

#     print(number, end=" ")