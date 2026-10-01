from gui_validator import *

def national_id_validator(id):
    if national_id.validate(id):
        print(national_id.find_place(id))
    else:
        print("error : invalid national id")

def phone_number_validator(phone):
    if phone_number.validate(phone):
        print(phone_number.operator_data(phone))
    else:
        print("error : invalid phone number")

def card_number_validator(card):
    if card_number.validate(card):
        print(card_number.bank_data(card))
    else:
        print("error : invalid card number")

def plate_validator(car_plate):
    if plate.is_valid(car_plate):
        print(plate.get_info(car_plate))
    else:
        print("error : invalid plate")

def bill_detail(bill_id, payment_id):
    print(bill.get_detail(bill_id , payment_id))