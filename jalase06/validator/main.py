from jalase06.validator import *

file_name = "validator.data"

while True:
    option = show_menu()
    print("-----------------------------------------------")

    match option:
        case 1:
            id = get_national_id()
            national_id_validator(id)
            write_to_file(file_name, id)
        case 2:
            phone_number = get_phone_number()
            phone_number_validator(phone_number)
            write_to_file(file_name, phone_number)
        case 3:
            card = get_card_number()
            card_number_validator(card)
            write_to_file(file_name, card)
        case 4:
            plate = get_plate()
            plate_validator(plate)
            write_to_file(file_name, plate)
        case 5:
            bill_id = get_bill_id()
            payment_id = get_payment_id()
            bill_detail(bill_id, payment_id)
            write_to_file(file_name, bill_id)
            write_to_file(file_name, payment_id)
        case 0:
            break
        case _:
            print("error : invalid option")

    print("-----------------------------------------------")