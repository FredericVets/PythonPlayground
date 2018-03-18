class Animal:
    def __init__(self, name, height, weight, sound):
        self.name = str(name)
        self.height = int(height)
        self.weight = float(weight)
        self.sound = str(sound)

    def make_sound(self, how_many=None):
        if how_many is None:
            return self.sound

        return (self.sound + " ") * how_many

    def give_paw(self, left=False, right=False):
        if left and right:
            raise ValueError("Can't give 2 paws : I'll fall!")

        PAW_RESULT = "{} is giving {} paw"
        if left:
            return PAW_RESULT.format(self.name, "left")
        if right:
            return PAW_RESULT.format(self.name, "right")

    def to_string(self):
        return "{0} is {1} cm tall and {2:.2f} kilograms and says {3}".format(
            self.name,
            self.height,
            self.weight,
            self.sound)


class Dog(Animal):
    def __init__(self, name, height, weight, sound, owner):
        # The preferred way to call the constructor of the super class.
        super().__init__(name, height, weight, sound)
        # Alternatives :
        # super(Dog, self).__init__(name, height, weight, sound)
        # Animal.__init__(self, name, height, weight, sound)
        self.owner = owner

    def to_string(self):
        return "{} and is owned by {}".format(
            super().to_string(),
            self.owner)


class Foo:
    pass


def print_animal(animal):
    print(type(animal))
    print(animal.to_string())


cat = Animal("Whiskers", 33, 10, "Meow")
print_animal(cat)
print(cat.make_sound(4))
print(cat.give_paw(right=True))

fido = Dog("Fido", 100, 30, "Ruff", "John")
print_animal(fido)
print(fido.name)
print(fido.give_paw(True))

duck = Foo()
duck.to_string = lambda: "If it walks like a duck and quacks like a duck, it IS a duck!"
print_animal(duck)


# In languages that use multiple inheritance, the order in which base classes are searched when looking for a method is
# often called the Method Resolution Order, or MRO. (In Python this also applies to other attributes.)
# http://python-history.blogspot.be/2010/06/method-resolution-order.html
class First:
    def __init__(self):
        print("First")


class Second(First):
    def __init__(self):
        super().__init__()
        print("Second")


# class Third(Second) will generate an error because MRO is not clear, when used in Fourth.
class Third(First):
    def __init__(self):
        super().__init__()
        print("Third")


class Fourth(Second, Third):
    def __init__(self):
        super().__init__()
        print("Fourth")


something = Fourth()

