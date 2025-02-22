def welcome():
    name_visitor = input("请输入你的名字： ")
    print("欢迎:" + name_visitor)
    return

def shop_info():
    address = "大学城"
    schedule = "周一到周五 10h-18h"
    print("位置在：" + address + "\n时间为：" + schedule)
    other = input("还有其他操作吗？(y/n)").lower()
    if other == 'y':
        choose_category()
    else:
        print("再见！")
    return

def order_management():
    print("这是订单管理页面。")
    client_name = input("请输入订单上的用户名字：")
    order_number = input("请输入订单号： ")

def choose_category():
    print('**** 菜单 ****\n[1] 营业时间\n[2] 订单管理'
          '\n[3] 物流追踪\n[4] 商品推荐 \n[5] 其他选项')
    choice = int(input("请输入你要的操作："))
    if choice == 1:
        # 营业时间
        shop_info()
    elif choice == 2:
        # 订单管理
        order_management()
    elif choice == 3:
        print("物流追踪")
    elif choice == 4:
        print("商品推荐")
    elif choice == 5:
        print("其他选项")
    else:
        print("您输入的操作有误，请重新输入！")
    return choice

welcome()
choose_category()