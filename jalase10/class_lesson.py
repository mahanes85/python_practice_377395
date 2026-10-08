class Lesson:
    def __init__(self, code, name, teacher):
        self.code = code
        self.name = name
        self.teacher = teacher

    def save(self):
        print(f"code : {self.code}")
        print(f"name : {self.name}")
        print(f"teacher : {self.teacher}")
        print("Saved")

    def edit(self, name, teacher):
        if name:
            self.name = name
        if teacher:
            self.teacher = teacher
        print("Changed")

    def __repr__(self):
        return f"name : {self.name}, teacher : {self.teacher}"

lesson1 = Lesson(123, "Python", "Ahmad")
lesson1.save()
lesson1.edit("Advance Python", "Omid")
print(lesson1)