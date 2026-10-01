from tkinter import *
from tkinter import messagebox

x_start = 20
y_start = 20
x_distance = 100
y_distance = 40

product =[]
def reset_form():
    name.set("")
    quantity.set(0)
    price.set(0)

def save_click():
    try:
        data = {
            "name" : name.get(),
            "quantity" : quantity.get(),
            "price" : price.get()
        }

        total_cost = sum(map(lambda item: item["quantity"] * item["price"], product))
        total_cost += quantity.get() * price.get()

        if total_cost <= 1000000:
            product.append(data)
            messagebox.showinfo("Saved", "Product Saved")
            reset_form()
        else:
            raise ValueError("More than budget")

    except Exception as e:
        messagebox.showerror("Error", f"Error {e}")


window = Tk()

window.title("product")
window.geometry("500x250")

Label(window, text= "Product Name").place(x = x_start, y = y_start)
name = StringVar()
Entry(window, textvariable= name).place(x = x_start + x_distance, y = y_start)

Label(window, text= "Quantity").place(x = x_start, y = y_start + y_distance)
quantity = IntVar()
Entry(window, textvariable= quantity).place(x = x_start + x_distance, y = y_start + y_distance)

Label(window, text= "Price").place(x = x_start , y = y_start + 2*y_distance)
price = IntVar()
Entry(window, textvariable= price).place(x = x_start + x_distance, y = y_start + 2*y_distance)

Button(window, text= "Save Product", command=save_click).place(x = x_start + 3.2*x_distance, y = y_start + y_distance)

window.mainloop()