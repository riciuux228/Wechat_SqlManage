import pygame

# 初始化游戏
pygame.init()

# 游戏窗口的宽度和高度
window_width = 800
window_height = 600

# 定义颜色
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 255, 0)

# 定义方格的大小和行列数
block_size = 50
num_rows = 10
num_cols = 10

# 定义游戏地图，0表示空地，1表示墙，2表示箱子，3表示目标点，4表示玩家
game_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 2, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# 加载图片
player_img = pygame.image.load("img.png")
wall_img = pygame.image.load("img_1.png")
box_img = pygame.image.load("img_2.png")
target_img = pygame.image.load("img.png")

# 设置游戏窗口
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("推箱子")

# 创建玩家类
class Player:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def move(self, drow, dcol):
        new_row = self.row + drow
        new_col = self.col + dcol
        if game_map[new_row][new_col] == 0 or game_map[new_row][new_col] == 3:
            self.row = new_row
            self.col = new_col
        elif game_map[new_row][new_col] == 2:
            new_row_box = new_row + drow
            new_col_box = new_col + dcol
            if game_map[new_row_box][new_col_box] == 0 or game_map[new_row_box][new_col_box] == 3:
                self.row = new_row
                self.col = new_col
                game_map[new_row_box][new_col_box] = 2
                game_map[new_row][new_col] = 0

    def draw(self):
        window.blit(player_img, (self.col * block_size, self.row * block_size))

# 创建游戏地图类
class GameMap:
    def draw(self):
        for row in range(num_rows):
            for col in range(num_cols):
                if game_map[row][col] == 1:
                    window.blit(wall_img, (col * block_size, row * block_size))
                elif game_map[row][col] == 2:
                    window.blit(box_img, (col * block_size, row * block_size))
                elif game_map[row][col] == 3:
                    window.blit(target_img, (col * block_size, row * block_size))

# 创建玩家对象和游戏地图对象
player = Player(4, 4)
game_map = GameMap()

# 游戏循环
running = True
while running:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.move(-1, 0)
            elif event.key == pygame.K_DOWN:
                player.move(1, 0)
            elif event.key == pygame.K_LEFT:
                player.move(0, -1)
            elif event.key == pygame.K_RIGHT:
                player.move(0, 1)

    # 绘制游戏窗口和游戏元素
    window.fill(black)
    game_map.draw()
    player.draw()
    pygame.display.update()

# 退出游戏
pygame.quit()
