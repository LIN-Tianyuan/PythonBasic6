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
    transfer_Elliot()
    return

def transfer_Elliot():
    print("非常好！我去检查一下订单情况！")
    return

def tracking_deliveries():
    print("我们很抱歉，您的订单有问题。")
    client_name = input("请输入订单上的用户名字：")
    order_number = input("请输入订单号： ")
    follow = input("请输入您的订单问题：")
    transfer_Christine()
    return

def transfer_Christine():
    print("谢谢您提供的细节。我们将核实情况后与您进行反馈！")
    return

def service_marketing():
    print("转接到相关人员为您做推荐！")
    transfer_Raoul()

def transfer_Raoul():
    suggestion_marketing = input("请问您需要我给您推荐什么方面的产品？")
    return

def others():
    transfer_Therese()
    return

def transfer_Therese():
    other_info = input("请问您需要什么其他信息？")
    return

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
        # 物流追踪
        tracking_deliveries()
    elif choice == 4:
        # 商品推荐
        service_marketing()
    elif choice == 5:
        # 其他选项
        others()
    else:
        print("您输入的操作有误，请重新输入！")
    return choice

welcome()
choose_category()