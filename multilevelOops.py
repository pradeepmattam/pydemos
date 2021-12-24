class Animal:
    def __init__(self):
        pass

    def living(self):
        print('Animal is living')


class Dog(Animal):
    def __init__(self):
        pass

    def living(self):
        print('Dog is living')


class Labrador(Dog):
    def __init__(self):
        pass


lab = Labrador()
lab.living()
