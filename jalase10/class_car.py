class Car:
    def __init__(self, name, color, plate):
        self.name = name
        self.color = color
        self.plate = plate

    def save(self):
        print(f"name : {self.name}")
        print(f"color : {self.color}")
        print(f"plate : {self.plate}")
        print("Saved")

    def change_plate(self, plate):
        if plate:
            self.plate = plate
        print("Changed")

    def __repr__(self):
        return f"plate : {self.plate}"

car1 = Car("Benz", "black", "12D345")
car1.save()
car1.change_plate("56D789")
print(car1)