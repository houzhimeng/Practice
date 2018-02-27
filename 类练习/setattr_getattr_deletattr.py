class Foo:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show(self):
        return "%s-%s" %(self.name,self.age)


obj = Foo('hou',18)
# print(obj.name)

# fun = getattr(obj, 'name')
# print(fun)

fun = getattr(obj, 'show')
print(obj,'show')

setattr(obj,'k1','v1')
print(obj.k1)