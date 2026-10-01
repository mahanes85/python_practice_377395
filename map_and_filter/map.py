from persiantools import digits

lesson_list = [
    {"name":"Java", "unit":3, "teacher":"Omid"},
    {"name":"Java", "unit":4, "teacher":"Ahmad"},
    {"name":"Python", "unit":5, "teacher":"Reza"},
    {"name":"Html", "unit":3, "teacher":"Ali"},
    {"name":"Css", "unit":5, "teacher":"Mohsen"}
]

new_lesson_1 = {"name":"Python", "unit":5, "teacher":"Reza"}
new_lesson_2 = {"name":"Java", "unit":3, "teacher":"Omid"}
new_lesson_3 = {"name":"Css", "unit":2, "teacher":"Mohsen"}

student_list = []

def check_lesson(lesson_list):
    if new_lesson_1 in lesson_list:
        student_list.append(new_lesson_1)
    if new_lesson_2 in lesson_list:
        student_list.append(new_lesson_2)
    if new_lesson_3 in lesson_list:
        student_list.append(new_lesson_3)
    return student_list

print(check_lesson(lesson_list))

result = sorted(student_list, key=lambda student_list : student_list["unit"])
print(result)

result = sorted(student_list, key=lambda student_list : student_list["name"])
print(result)

def price(student_list):
    if student_list["unit"] == 5:
        student_list["price"] = 1400
    if student_list["unit"] == 3:
        student_list["price"] = 1200
    if student_list["unit"] == 2:
        student_list["price"] = 1000
    return student_list

result = list(map(price, student_list))
print(result)

total_cost = sum(map(lambda student_list : student_list["price"], student_list))
print("total cost :", total_cost)

print("total cost :", digits.to_word(total_cost))