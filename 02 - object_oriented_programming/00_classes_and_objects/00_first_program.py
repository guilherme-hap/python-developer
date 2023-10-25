class Bicycle:
    def __init__(self, color, model, year, value):
        self.color = color
        self.model = model
        self.year = year
        self.value = value

    def honk(self):
        print("Plim plim...")

    def stop(self):
        print("Stoping bicycle...")
        print("Bicycle stoped!")

    def run(self):
        print("Vrummmmm...")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{key}={value}' for key, value in self.__dict__.items()])}"


b1 = Bicycle("red", "caloi", 2022, 600)
b1.honk()
b1.run()
b1.stop()
print(b1.color, b1.model, b1.year, b1.value)

b2 = Bicycle("green", "monark", 2000, 189)
print(b2)
b2.run()