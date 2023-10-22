def show_message():
    print("Hello world!")


def show_message_2(name):
    print(f"Welcome {name}!")


def show_message_3(name="Anônimo"):
    print(f"Welcome {name}!")


show_message()
show_message_2(name="Guilherme")
show_message_3()
show_message_3(name="Chappie")