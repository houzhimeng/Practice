class F:
    def f1(self):
        print('F.f1')

    def f2(self):
        print('F.f2')

class S(F):
    def s1(self):
        print('S.s1')

obj = S()
obj.s1()
obj.f1()
