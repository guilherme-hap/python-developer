class Animal:
    def __init__(self, nbr_paws):
        self.nbr_paws = nbr_paws

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{key}={value}' for key, value in self.__dict__.items()])}"


class Platypus(Animal):
    def __init__(self, fur_color, **kw):
        self.fur_color = fur_color
        super().__init__(**kw)


class Bird(Animal):
    def __init__(self, beak_color, **kw):
        self.beak_color = beak_color
        super().__init__(**kw)


class Cat(Platypus):
    pass


class Platypus(Platypus, Bird):
    def __init__(self, beak_color, fur_color, nbr_paws):
        super().__init__(fur_color=fur_color, beak_color=beak_color, nbr_paws=nbr_paws)


cat = Cat(nbr_paws=4, fur_color="Black")
print(cat)

platypus = Platypus(nbr_paws=2, fur_color="red", beak_color="orange")
print(platypus)