parking_list = []

def show_menu():
    print("1) enter to parking")
    print("2) parking list")
    print("3) search car by plate")
    print("4) exit")
    option = int(input("option :"))
    return option

def get_car_information():
    name = input("enter car name :")
    color = input("enter car color :")
    plate = input("enter car plate :")
    enter_time = input("enter time :")
    return {"name":name , "color":color , "plate":plate , "enter_time":enter_time}

def print_parking_list(parking_list):
    print("parking list")
    for car in parking_list:
        print(f"{car['name']:10} {car['color']:10} {car['plate']:10} {car['enter_time']:10}")

def search_car_by_plate(parking_list , plate):
    for car in parking_list:
        if car["plate"] == plate:
            return car