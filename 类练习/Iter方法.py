class Foo:

    def __init__(self,name,age):
        self.name = name
        self.age = age


    def __iter__(self):
        return iter([11,22,33])

li = Foo('hou',18)

for i in li:
    print(i)

