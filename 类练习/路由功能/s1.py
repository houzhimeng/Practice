import s2

inp = input('请输入要查看的网页:')

if hasattr(s2, inp):
    func = getattr(s2, inp)
    result = func()
    print(result)
else:
    print('404')