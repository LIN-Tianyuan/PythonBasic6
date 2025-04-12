# 导包
import pygame
import sys

# 初始化
pygame.init()

# 窗口 set_mode 设置尺寸
screen = pygame.display.set_mode((400, 400))
screen.fill((255, 182, 193))
# 设置标题
pygame.display.set_caption("My first game")
# 设置字体
f = pygame.font.SysFont("Arial", 50)
# 设置文字 第一个参数：文本 第二个参数：是否顺滑 第三个参数：文字的颜色 第四个参数：背景色
text = f.render("Happy game", True, (0, 255, 0), (0, 0, 0))
# 获取文本框
text_rect = text.get_rect()
# 文本框的位置
text_rect.center = (200, 200)
# 把文本框画到窗口上
screen.blit(text, text_rect)
while True:
    # 获取所有的事件
    for event in pygame.event.get():
        # 判断一下这个事件是不是一个退出事件
        # 点击×说明触发了退出事件
        if event.type == pygame.QUIT:
            # 卸载pygame模块
            pygame.quit()
            # 终止进程
            sys.exit()
    # 刷新屏幕
    pygame.display.flip()



