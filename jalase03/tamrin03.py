num_list = []

for num in range(2,101,2):
    if num % 7 == 0:
        num_list.append(num)

print(f"even Numbers divisible by 7 : {num_list}")