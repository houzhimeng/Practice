class hou:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def foo(self):
        print('{}----{}'.format(self.name,self.age))

Hou = hou('houzhimeng',19)
Hou.foo()


Li = hou('lishou',22)
Li.foo()