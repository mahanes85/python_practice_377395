from contact_module import *

while True:
    option = show_menu()
    print("-----------------------------------")

    match option:

        case 1:
            contact = get_contact()
            if search_by_phone(contact_list , contact["phone"]):
                print("error : contact already exist")
            else:
                contact_list.append(contact)
                print("info : contact added")

        case 2:
            print_contact_list(contact_list)

        case 3:
            phone = int(input("enter a phone number for search : "))
            result = search_by_phone(contact_list, phone)
            if result:
                print("contact found :", result)
            else:
                print("error : contact not found")

        case 4:
            break

        case _:
            print("error : invalid option")

    print("-----------------------------------")