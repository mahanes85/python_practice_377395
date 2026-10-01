from jalase06.validator import *

def show_menu():
    print("1) national id:")
    print("2) phone_number:")
    print("3) bank card number:")
    print("4) plate:")
    print("5) bill:")
    print("0) exit:")
    return int(input("enter option:"))

def get_national_id():
    national_id = input("enter national id :")
    return  national_id

def get_phone_number():
    phone_number = input("enter phone number :")
    return phone_number

def get_card_number():
    card_number = input("enter card number :")
    return card_number

def get_plate():
    plate = input("enter plate :")
    return plate

def get_bill_id():
    bill_id = input("enter bill id :")
    return bill_id

def get_payment_id():
    payment_id = input("enter payment id :")
    return payment_id

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