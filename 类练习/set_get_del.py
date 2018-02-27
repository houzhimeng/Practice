class Foo:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __getitem__(self, item):
        return item + 8


    def __setitem__(self, key, value):
        print(key,value)

    def __delitem__(self, key):
        print(key)



li = Foo('hou',18)
print(li.name)

r = li[8]
print(r)

li[100] = 'abcdefg'

del li[10]