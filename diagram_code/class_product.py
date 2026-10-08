class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def test(self):
        print(f"name : {self.name}")
        print(f"price : {self.price}")

    def __repr__(self):
        return f"name : {self.name} , price : {self.price}"

class NonElectric(Product):
    def __init__(self, weight):
        self.weight = weight

    def test(self):
        print(f"weight : {self.weight}")

    def __repr__(self):
        return f"weight : {self.weight}"

class Furniture(NonElectric):
    def __init__(self, num_person, color):
        self.num_person = num_person
        self.color = color

    def test(self):
        print(f"num_person : {self.num_person}")
        print(f"color : {self.color}")

    def __repr__(self):
        return f"person : {self.num_person} , color : {self.color}"

class Electrical(Product):
    def __init__(self, voltage):
        self.voltage = voltage

    def test(self):
        print(f"voltage : {self.voltage}")

    def __repr__(self):
        return f"voltage : {self.voltage}"

class Laptop(Electrical):
    def __init__(self, ram, cpu):
        self.ram = ram
        self.cpu = cpu

    def test(self):
        print(f"ram : {self.ram}")
        print(f"cpu : {self.cpu}")

    def __repr__(self):
        return f"ram : {self.ram} , cpu : {self.cpu}"

class Mobile(Electrical):
    def __init__(self, screen_size):
        self.screen_size = screen_size

    def test(self):
        print(f"screen size : {self.screen_size}")

    def __repr__(self):
        return f"screen_size : {self.screen_size}"

class Iphone(Mobile):
    def __init__(self, series):
        self.series = series

    def test(self):
        print(f"series : {self.series}")

    def __repr__(self):
        return f"series : {self.series}"

class Samsung(Mobile):
    def __init__(self, series):
        self.series = series

    def test(self):
        print(f"series : {self.series}")

    def __repr__(self):
        return f"series : {self.series}"

product = Product("cellphone", 1200)
product.test()

electrical = Electrical(5)
electrical.test()

mobile = Mobile("12 inch")
mobile.test()

samsung = Samsung("A21")
samsung.test()

product = Product("sofa", 2500)
product.test()

nonelectrical = NonElectric("12 kg")
nonelectrical.test()

forniture = Furniture(7 ,"red")
forniture.test()