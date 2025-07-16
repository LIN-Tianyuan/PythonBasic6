# 导包
import pygame
import sys
import random

# 窗口的长
window_x = 720
# 窗口的宽
window_y = 480
# 蛇的速度
snake_speed = 10
# 初始化游戏
pygame.init()
# 设置窗口的大小
game = pygame.display.set_mode((window_x, window_y))
# 设置标题
pygame.display.set_caption("Snake")

# FPS（每秒帧数）控制器
fps = pygame.time.Clock()

# 定义蛇的默认位置
snake_position = [100, 50]
# 定义蛇的前4块
snake_body = [
    [100, 50],
    [90, 50],
    [80, 50],
    [70, 50]
]

a = random.randint(0, 72)
b = random.randint(0, 48)
# 水果的位置
fruit_position = [a * 10, b * 10]

# 蛇要转的方向
change_to = 'RIGHT'
# 蛇一开始的方向
direction = 'RIGHT'


while True:
    # 获取所有的事件
    for event in pygame.event.get():

        # 控制键盘事件
        if event.type == pygame.KEYDOWN:
            # 键盘按了上键
            if event.key == pygame.K_UP:
                # 蛇改变的方向
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

        # 判断事件是不是退出事件
        if event.type == pygame.QUIT:
            # 游戏退出，关闭相关组件
            pygame.quit()
            sys.exit()

    # 当按了左键时，同时要判断蛇的现有方向是不是 不是往右
    if change_to == 'LEFT' and direction != 'RIGHT':
        # 就让蛇的现有方向改成向左
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'

    # 当方向是往右时
    if direction == 'RIGHT':
        # 蛇的位置往右变换
        snake_position[0] = snake_position[0] + 10
    if direction == 'LEFT':
        snake_position[0] = snake_position[0] - 10
    if direction == 'UP':
        snake_position[1] = snake_position[1] - 10
    if direction == 'DOWN':
        snake_position[1] = snake_position[1] + 10


    # 蛇变长
    snake_body.insert(0, list(snake_position))
    print(snake_position)
    print(fruit_position)
    # 吃苹果
    if snake_position == fruit_position:
        # 刷新新的苹果
        fruit_position = [random.randint(0, 72) * 10, random.randint(0, 48) * 10]
    else:
        # 去掉最后一块
        snake_body.pop(4)

    game.fill((0, 0, 0))
    # 画蛇
    for pos in snake_body:
        pygame.draw.rect(game, (0, 0, 255), pygame.Rect(pos[0], pos[1], 10, 10))

    # 画苹果
    pygame.draw.rect(game, (255, 0, 0), pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))
    # 刷新页面
    pygame.display.flip()

    fps.tick(snake_speed)
