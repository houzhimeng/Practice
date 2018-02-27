class Foo:

    def bar(self):
        print('bar')

    @staticmethod
    def sta():
        print('sta')

    @staticmethod
    def sta1(a1,a2):
        print(a1,a2)

    @classmethod
    def classmd(cls):
        print('classmd')

print(Foo.sta())
Foo.sta1(1,2)
print(Foo.classmd())