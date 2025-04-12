# 导包
import pygame
import sys
import random

window_x = 720
window_y = 480
# 初始化游戏
pygame.init()
# 设置窗口的大小
game = pygame.display.set_mode((window_x, window_y))
# 设置标题
pygame.display.set_caption("Snake")

# 定义蛇的默认位置
snake_position = [100, 50]
# 定义蛇的前4块
snake_body = [
    [100, 50],
    [90, 50],
    [80, 50],
    [70, 50]
]
a = random.randint(0, 720)
b = random.randint(0, 480)
# 水果的位置
fruit_position = [a, b]


while True:
    # 获取所有的事件
    for event in pygame.event.get():
        # 判断事件是不是退出事件
        if event.type == pygame.QUIT:
            # 游戏退出，关闭相关组件
            pygame.quit()
            sys.exit()

    # 画蛇
    for pos in snake_body:
        pygame.draw.rect(game, (0, 0, 255), pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(game, (255, 0, 0), pygame.Rect(a, b, 10, 10))
    # 刷新页面
    pygame.display.flip()
