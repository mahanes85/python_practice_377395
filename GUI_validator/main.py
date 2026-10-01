from GUI_validator import *
from GUI_validator.module import *

x_start = 30
y_start = 30
x_distance = 120
y_distance = 40

data_list = []

def reset_form():
    national_id.set("")
    phone_number.set("")
    bank_card_number.set("")
    plate.set("")
    bill_id.set("")
    payment_id.set("")

def save_click():
    try:
        data = {
            "national_id": national_id_validator(national_id.get()),
            "phone": phone_number_validator(phone_number.get()),
            "card_number": card_number_validator(bank_card_number.get()),
            "plate": plate_validator(plate.get()),
            "bill_id": bill_detail(bill_id.get(), payment_id.get()),
            }
        data_list.append(data)
        messagebox.showinfo("saved", "data aved")
        reset_form()
    except Exception as e:
        messagebox.showerror("Error", f"Error {e}")

window = Tk()

window.title("validator")
window.geometry("500x300")

Label(window, text = "National Id").place(x = x_start, y = y_start)
national_id = StringVar()
Entry(window, textvariable=national_id).place(x = x_start + x_distance, y = y_start)

Label(window, text = "Phone Number").place(x = x_start, y = y_start + y_distance)
phone_number = StringVar()
Entry(window, textvariable=phone_number).place(x = x_start + x_distance, y = y_start + y_distance)

Label(window, text = "Bank Card Number").place(x = x_start, y = y_start + 2*y_distance)
bank_card_number = StringVar()
Entry(window, textvariable=bank_card_number).place(x = x_start + x_distance, y = y_start + 2*y_distance)

Label(window, text = "Plate").place(x = x_start, y = y_start + 3*y_distance)
plate = StringVar()
Entry(window, textvariable=plate).place(x = x_start + x_distance, y = y_start + 3*y_distance)

Label(window, text = "Bill Id").place(x = x_start, y = y_start + 4*y_distance)
bill_id = StringVar()
Entry(window, textvariable=bill_id).place(x = x_start + x_distance, y = y_start + 4*y_distance)

Label(window, text = "Payment Id").place(x = x_start, y = y_start + 5*y_distance)
payment_id = StringVar()
Entry(window, textvariable=payment_id).place(x = x_start + x_distance, y = y_start + 5*y_distance)

Button(window, text = "Query", command=save_click, font = 20,
       width = 10 , height = 2).place(x = x_start + 2.5*x_distance, y = y_start + 2*y_distance)

window.mainloop()