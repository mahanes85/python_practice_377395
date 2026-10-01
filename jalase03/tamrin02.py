odd_list = []
even_list = []

while True:
    num = int(input("enter a number :"))
    if num == 0:
        break
    elif num % 2 == 0:
        even_list.append(num)
        even_list.sort()
    else:
        odd_list.append(num)
        odd_list.sort()

print(f"list of odd numbers : {odd_list}")
print(f"list of even numbers : {even_list}")