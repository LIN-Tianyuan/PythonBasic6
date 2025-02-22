# 定义函数
def greet(name):
    print("Hello, " + name)

greet("alex")
greet("jack")
greet("luna")

# 参数
def greet2(firstname, lastname):
    print("Hello, " + lastname + " " + firstname)

greet2("lin", "tianyuan")

# 默认参数
def season_pref(season="Spring"):
    print("My favourite season is: " + season)

season_pref()
season_pref("Summer")

print("----------")

# 不定长参数
def visit(*country):
    print(country)

visit("France")
visit("Spain", "China")
visit("America", "Germany", "Japan")

print("----------")

def list_game(competitor_1, competitor_2, competitor_3):
    print("今天参赛的人是：" + competitor_1 + " " + competitor_2 + " " + competitor_3)

# 位置参数
list_game("Alex", "Jack", "Luna")
# 关键字参数
list_game(competitor_2="Alex", competitor_3="Jack", competitor_1="Luna")
