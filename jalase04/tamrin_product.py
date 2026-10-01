product_list = []
total_cost = 0

while True:
    name = input("write a name :")
    quantity = int(input("enter a quantity :"))
    price = int(input("enter a price"))

    product = {
        "name":name,
        "quantity":quantity,
        "price":price
    }

    total_cost += price * quantity

    if total_cost <= 1000000:
        product_list.append(product)
        print("saved")
        print("-------------------")
    else:
        print("more than budget")
        break

for product in product_list:
    print(f"{product['name']:10} {product['quantity']:10} {product['price']}")