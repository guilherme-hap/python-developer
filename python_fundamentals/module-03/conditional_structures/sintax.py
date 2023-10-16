ADULT = 18
SPECIAL_AGE_CASE = 17

age = int(input("How old are you: "))

if age >= ADULT:
    print("Adult, can get a driver's licence.")

if age < ADULT:
    print("Can't get a driver's licence.")


if age >= ADULT:
    print("Adult, can get a driver's licence.")
else:
    print("Can't get a driver's licence.")


if age >= ADULT:
    print("Adult, can get a driver's licence.")
elif age == SPECIAL_AGE_CASE:
    print("Can take theory classes, but still can't take practical classes.")
else:
    print("Can't get a driver's licence.")