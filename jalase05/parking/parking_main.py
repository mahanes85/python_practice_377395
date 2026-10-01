from parking_module import *

while True:
    option = show_menu()
    print("---------------------------")

    match option:
        case 1:
            car = get_car_information()
            if search_car_by_plate(parking_list , car["plate"]):
                print("error : car already exists")
            else:
                parking_list.append(car)
                print("info : car added to parking")

        case 2:
            print_parking_list(parking_list)

        case 3:
            plate = input("enter the plate number :")
            result = search_car_by_plate(parking_list , plate)
            if result:
                print("info : car found :", result)
            else:
                print("error : car not found")

        case 4:
            break

        case _:
            print("error : invalid option")

    print("---------------------------")