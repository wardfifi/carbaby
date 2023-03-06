#Car.py

class Car:
    def __init__(self, make = "", model = "", year = 0, price = 0):
        self.make = make.upper()
        self.model = model.upper()
        self.year = year
        self.price = price

    def __gt__(self, rhs):
        if self.make == rhs.make:
            if self.model == rhs.model:
                if self.year == rhs.year:
                    return self.price > rhs.price
                else:
                    return self.year > rhs.year
                
            else:
                return self.model > rhs.model
        else:
            return self.make > rhs.make
    
    def __lt__(self, rhs):
        if self.make == rhs.make:
            if self.model == rhs.model:
                if self.year == rhs.year:
                    return self.price < rhs.price
                else:
                    return self.year < rhs.year
            else:
                return self.model < rhs.model
        else:
            return self.make < rhs.make

    def __eq__(self, rhs):
        if (self.make == rhs.make) and (self.model == rhs.model) and (self.year == rhs.year) and (self.price == rhs.price):
            return True
        else:
            return False

    def __str__(self):
        return "Make: {}, Model: {}, Year: {}, Price: ${}"\
            .format(self.make.upper(), self.model.upper(), self.year, self.price)