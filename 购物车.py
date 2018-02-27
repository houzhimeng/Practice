import datetime

product_list = [
    ('Iphone', 5800),
    ('Mac Pro', 16000),
    ('Bike', 800),
    ('Watch', 12000),
    ('Coffee', 30),
    ('Book', 21),
]

shopping_list = []
salary = input('Input are you money:')



if salary.isdigit():
    salary = int(salary)

    while True:
        for index, item in enumerate(product_list):
            print(index, item)
        user_choice = input("买什么:")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice < len(product_list) and user_choice >= 0:
                p_item = product_list[user_choice]
                if p_item[1] <= salary:
                    shopping_list.append(p_item)
                    salary -= p_item[1]
                    print("Add %s into shopping cart,you current balance is %s" %(p_item, salary))
                else:
                    print('没钱了,只剩下:{0}'.format(salary))
            else:
                print('商品不存在')
        elif user_choice == 'q':
            print(shopping_list)
            for p in shopping_list:
                print(p)
            print('你的余额还剩下:', salary)
            exit()

        else:
            print('invalid option')


