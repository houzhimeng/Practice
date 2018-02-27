class Province:
    country = '中国'

    def __init__(self,name):
        self.name = name


beijing = Province('北京')
print(Province.country)
print(beijing.name)