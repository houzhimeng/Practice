class Tearch:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.salary = 1000

class Course:
    def __init__(self,name,teacher,cost):
        self.name = name
        self.teacher = teacher
        self.cost = cost


    def class_up(self):
        self.teacher.salary += self.cost




t1 = Tearch('侯',18)
t2 = Tearch('王',19)
t3 = Tearch('李',20)

c1 = Course('数学',t1,1)
print(c1.name)
print(c1.teacher.name)
print(c1.teacher.salary)

c1.class_up()
print(c1.teacher.salary)