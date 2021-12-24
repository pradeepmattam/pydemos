class Car:
    wheels = 4

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def drive(self):
        print('driving '+self.make+' '+self.model)
        return self

    def stop(self):
        print('stopping '+self.make+' '+self.model)
        return self
