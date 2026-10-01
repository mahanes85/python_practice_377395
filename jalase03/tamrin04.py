num_list = []

while True:
    num = int(input("enter a number :"))
    if num == 0:
        break
    elif num % 2 != 0:
        num_list.append(num)

if num_list:
    avg = sum(num_list) / len(num_list)
    print(f"list of odd numbers : {num_list}")
    print(f"average of odd numbers : {avg}")
else:
    print("no odd number entered")