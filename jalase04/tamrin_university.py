lesson_list=[]
total_unit = 0

while True:
    title = input("write a lesson title :")
    teacher = input("write a teacher name:")
    duration = int(input("enter the duration:"))
    unit = int(input("enter a unit:"))

    lesson = {
        "title":title,
        "teacher":teacher,
        "duration":duration,
        "unit":unit
    }

    total_unit += unit

    if total_unit <= 17:
        lesson_list.append(lesson)
        print("Lesson Saved")
    else:
        print("Lesson Unit Max Reached !!!")
        break
    print("---------------------------------------")

for lesson in lesson_list:
    print(f"{lesson['title']:10} by {lesson['teacher']:20} ({lesson['unit']})")