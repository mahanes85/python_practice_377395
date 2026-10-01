contact_list = []

def show_menu():
    print("1)add contact")
    print("2)contact list")
    print("3)search by phone")
    print("4)exit")
    option = int(input("option:"))
    return option

def get_contact():
    name = input("enter a name : ")
    family_name = input("enter a family name : ")
    phone = int(input("enter a phone number : "))
    title = input("enter a title : ")
    return {"name" : name , "family_name" : family_name , "phone" : phone , "title" : title}

def print_contact_list(contact_list):
    for contact in contact_list:
        print(f"{contact['name']:10} {contact['family_name']:10} {contact['phone']:10} {contact['title']:10}")

def search_by_phone(contact_list , phone):
    for contact in contact_list:
        if contact["phone"] == phone:
            return contact