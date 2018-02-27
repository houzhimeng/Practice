try:
    li = [11,22]
    li[999]
except IndexError as e:
    print('IndexError',e)
except ValueError as e:
    print('ValueError',e)
except Exception as e:
    print('Exception',e)
else:
    print('else')
finally:
    print(.....)