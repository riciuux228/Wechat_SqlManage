import pygame
import random

# 初始化游戏
pygame.init()

# 游戏窗口的宽度和高度
window_width = 800
window_height = 600

# 定义颜色
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# 创建游戏窗口
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("贪吃蛇游戏")

# 定义蛇的初始位置和大小
snake_size = 20
snake_x = window_width // 2
snake_y = window_height // 2

# 定义蛇移动的初始速度
snake_speed = 8
snake_x_change = 0
snake_y_change = 0

# 定义食物的初始位置
food_size = 20
food_x = round(random.randrange(0, window_width - food_size) / 20) * 20
food_y = round(random.randrange(0, window_height - food_size) / 20) * 20

# 定义蛇的身体列表
snake_body = []
snake_length = 1

# 游戏结束标志
game_over = False

# 游戏循环
while not game_over:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_x_change = -snake_size
                snake_y_change = 0
            elif event.key == pygame.K_RIGHT:
                snake_x_change = snake_size
                snake_y_change = 0
            elif event.key == pygame.K_UP:
                snake_y_change = -snake_size
                snake_x_change = 0
            elif event.key == pygame.K_DOWN:
                snake_y_change = snake_size
                snake_x_change = 0

    # 更新蛇的位置
    snake_x += snake_x_change
    snake_y += snake_y_change

    # 判断蛇是否吃到食物
    if snake_x == food_x and snake_y == food_y:
        food_x = round(random.randrange(0, window_width - food_size) / 20) * 20
        food_y = round(random.randrange(0, window_height - food_size) / 20) * 20
        snake_length += 1

    # 绘制游戏窗口和蛇
    window.fill(black)
    pygame.draw.rect(window, red, [food_x, food_y, food_size, food_size])
    snake_head = []
    snake_head.append(snake_x)
    snake_head.append(snake_y)
    snake_body.append(snake_head)
    if len(snake_body) > snake_length:
        del snake_body[0]

    for segment in snake_body[:-1]:
        if segment == snake_head:
            game_over = True

    for segment in snake_body:
        pygame.draw.rect(window, white, [segment[0], segment[1], snake_size, snake_size])

    pygame.display.update()

    # 控制游戏帧率
    clock = pygame.time.Clock()
    clock.tick(snake_speed)

# 退出游戏
pygame.quit()
