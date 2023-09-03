import pygame
import random

# 初始化游戏
pygame.init()

# 游戏窗口的宽度和高度
window_width = 1500
window_height = 1000

# 定义颜色
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# 创建游戏窗口
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("飞机大战")

# 加载玩家飞机图片
player_img = pygame.image.load("img.png")
player_width = 80
player_height = 80

# 加载敌机图片
enemy_img = pygame.image.load("img_1.png")
enemy_width = 80
enemy_height = 80

# 加载子弹图片
bullet_img = pygame.image.load("img_2.png")
bullet_width = 20
bullet_height = 40

# 定义玩家飞机的初始位置
player_x = window_width // 2 - player_width // 2
player_y = window_height - player_height - 10

# 定义敌机列表
enemies = []
enemy_speed = 3

# 定义子弹列表
bullets = []
bullet_speed = 5

# 游戏分数
score = 0

# 游戏结束标志
game_over = False

# 创建玩家飞机函数
def create_player(x, y):
    window.blit(player_img, (x, y))

# 创建敌机函数
def create_enemy(x, y):
    window.blit(enemy_img, (x, y))

# 创建子弹函数
def create_bullet(x, y):
    window.blit(bullet_img, (x, y))

# 检测碰撞函数
def check_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    if bullet_x >= enemy_x and bullet_x <= enemy_x + enemy_width and bullet_y <= enemy_y + enemy_height:
        return True
    return False

# 游戏循环
while not game_over:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet_x = player_x + player_width // 2 - bullet_width // 2
                bullet_y = player_y
                bullets.append([bullet_x, bullet_y])

    # 移动玩家飞机
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= 5
    if keys[pygame.K_RIGHT] and player_x < window_width - player_width:
        player_x += 5

    # 移动子弹
    for bullet in bullets:
        bullet[1] -= bullet_speed
        if bullet[1] <= 0:
            bullets.remove(bullet)

    # 移动敌机
    for enemy in enemies:
        enemy[1] += enemy_speed
        if enemy[1] > window_height:
            enemies.remove(enemy)

    # 检测子弹与敌机的碰撞
    for bullet in bullets:
        for enemy in enemies:
            if check_collision(enemy[0], enemy[1], bullet[0], bullet[1]):
                bullets.remove(bullet)
                enemies.remove(enemy)
                score += 1

    # 生成敌机
    if random.randint(1, 100) == 1:
        enemy_x = random.randint(0, window_width - enemy_width)
        enemy_y = -enemy_height
        enemies.append([enemy_x, enemy_y])

    # 绘制游戏窗口和游戏元素
    window.fill(black)
    create_player(player_x, player_y)
    for enemy in enemies:
        create_enemy(enemy[0], enemy[1])
    for bullet in bullets:
        create_bullet(bullet[0], bullet[1])

    # 显示分数
    font = pygame.font.Font(None, 36)
    text = font.render("Score: " + str(score), True, white)
    window.blit(text, (10, 10))

    pygame.display.update()

# 退出游戏
pygame.quit()
