class Pergination:
    def __init__(self,current_page):
        try:
            p = int(current_page)
        except Exception as e:
            p = 1

        self.page = p

    @property
    def start(self):
        val = (self.page - 1) * 10
        return val

    @property
    def end(self):
        val = self.page * 10
        return val

li = []
for i in range(100):
    li.append(i)

while True:
    p = input('请输入页码:')
    obj = Pergination(p)
    print (li[obj.start:obj.end])
