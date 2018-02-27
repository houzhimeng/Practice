import time

def add_count(fun):
    def wrapper():
        print('call fun')
        fun()
    return wrapper


@add_count
def show_haha():
    print('haha')

show_haha()

"""
{}
"""

r'sdsdsdjhwjh{}{}ds'