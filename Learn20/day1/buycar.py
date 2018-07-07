#coding=utf-8
#__author:  bwzhang
#__date:    2018/6/4


product_list =[
    ('Mac',9000),
    ('kindle',800),
    ('tesla',900000),
    ('python book',105),
    ('bike',2000),
]


saving = input('please input your money:')
shopping_car = []
if saving.isdigit():
    saving = int(saving)
    while True:
        for i,v in enumerate(product_list,1):
            print(i,'####',v)
            choice = input("选择购买商品编号[退出：q]")


            if choice.isdigit() :
                choice = int(choice)
                if choice>0 and choice<=len(product_list):

                    p_item = product_list[choice-1]

                    if p_item[1] < saving:
                        saving-= p_item[1]
                        shopping_car.append(p_item)

                    else:
                        print('余额不足，还剩$s元钱'%saving)
                else:
                    print('编码不存在')
            elif choice =='q':
                print('你所购买的商品如下'.center(10,'#'))
                for i in shopping_car:
                    print (i)
                    print('你还剩余%s元钱'%saving)
                    break
            else:
                print('invalid input')