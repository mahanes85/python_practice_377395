name_list = []

while True:
    name = str(input("write a name :"))
    if name.lower() == "exit":
        break
    name = name.strip()
    name_list.append(name)
    name_list.sort()

print(f"list of the names : {name_list}")