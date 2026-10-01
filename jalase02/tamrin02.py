sum_num = 0
count = 0

for i in range (100,999,2):
    if i % 7 == 0:
        sum_num += i
        count += 1

average = sum_num/count

print("average :", average)