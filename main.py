import pygame, sys, random
from pygame.math import Vector2

class FRUIT:
    #create an x & y position
    #draw a square
    def __init__(self):
        self.randomise_pos()
    
    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.pos.x*cell_size,self.pos.y*cell_size,cell_size,cell_size)
        screen.blit(apple,fruit_rect)
        # pygame.draw.rect(screen,(255, 32, 78),fruit_rect)
    
    def randomise_pos(self):
        self.x = random.randint(0,cell_number-1)
        self.y = random.randint(0,cell_number-1)
        #use vectors to store x,y
        self.pos = Vector2(self.x,self.y)

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(1,0)
        self.new_block = False
        self.head = self.body[0]
        self.tail = self.body[-1]

        self.head_up = pygame.image.load('graphics/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('graphics/head_down.png').convert_alpha()
        self.head_right = pygame.image.load('graphics/head_right.png').convert_alpha()
        self.head_left = pygame.image.load('graphics/head_left.png').convert_alpha()
        
        self.tail_up = pygame.image.load('graphics/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('graphics/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('graphics/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('graphics/tail_left.png').convert_alpha()
        
        self.body_vertical = pygame.image.load('graphics/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('graphics/body_horizontal.png').convert_alpha()
        
        self.body_tr = pygame.image.load('graphics/body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load('graphics/body_tl.png').convert_alpha()
        self.body_br = pygame.image.load('graphics/body_br.png').convert_alpha()
        self.body_bl = pygame.image.load('graphics/body_bl.png').convert_alpha()
    
    def draw_snake(self):
        # for block in self.body:
        #     snake_rect = pygame.Rect(block.x*cell_size,block.y*cell_size,cell_size,cell_size)
        #     pygame.draw.rect(screen,(55, 140, 231),snake_rect)

        self.update_head()
        self.update_tail()
        for index,block in enumerate(self.body):
            #create rect
            x_pos = block.x*cell_size
            y_pos = block.y*cell_size
            block_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)

            #what direction is the head facing
            if index == 0:
                screen.blit(self.head,block_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail,block_rect)
            else:
                prev_block = self.body[index-1] - block
                next_block = self.body[index+1] - block
                if prev_block.x == next_block.x:
                    screen.blit(self.body_vertical,block_rect)
                elif prev_block.y == next_block.y:
                    screen.blit(self.body_horizontal,block_rect)
                else:
                    if prev_block.x == -1 and next_block.y == -1 or prev_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_tl,block_rect)
                    if prev_block.x == -1 and next_block.y == 1 or prev_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_bl,block_rect)
                    if prev_block.x == 1 and next_block.y == -1 or prev_block.y == -1 and next_block.x == 1:
                        screen.blit(self.body_tr,block_rect)
                    if prev_block.x == 1 and next_block.y == 1 or prev_block.y == 1 and next_block.x == 1:
                        screen.blit(self.body_br,block_rect)

    def move_snake(self):
        # new head = direction, remove last block of snake
        if self.new_block == True:
            body_copy = self.body
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy
    
    def grow_body(self):
        self.new_block = True

    def update_head(self):
        head_face = self.body[1] - self.body[0]
        if head_face == Vector2(1,0):
            self.head = self.head_left
        if head_face == Vector2(-1,0):
            self.head = self.head_right
        if head_face == Vector2(0,1):
            self.head = self.head_up
        if head_face == Vector2(0,-1):
            self.head = self.head_down
    
    def update_tail(self):
        head_face = self.body[-2] - self.body[-1]
        if head_face == Vector2(1,0):
            self.tail = self.tail_left
        if head_face == Vector2(-1,0):
            self.tail = self.tail_right
        if head_face == Vector2(0,1):
            self.tail = self.tail_up
        if head_face == Vector2(0,-1):
            self.tail = self.tail_down

class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
    
    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()
    
    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomise_pos()
            self.snake.grow_body()
    
    def check_fail(self):
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        pygame.quit()
        sys.exit()

    def draw_grass(self):
        grass_color = (155, 207, 83)
        for row in range(cell_number):
            if row % 2 == 0:
                for col in range(cell_number):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(col*cell_size,row * cell_size,cell_size,cell_size)
                        pygame.draw.rect(screen,grass_color,grass_rect)
            else:
                for col in range(cell_number):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(col*cell_size,row * cell_size,cell_size,cell_size)
                        pygame.draw.rect(screen,grass_color,grass_rect)

    def draw_score(self):
        score_str = "Score: " + str(len(self.snake.body) - 3)
        score_surface = font.render(score_str,True,pygame.Color('white'))
        score_x = cell_size * cell_number - 90
        score_rect = score_surface.get_rect(center=(score_x, 60))
        screen.blit(score_surface,score_rect)

pygame.init()

cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_size * cell_number, cell_size * cell_number))
pygame.display.set_caption('Snake')
clock = pygame.time.Clock()
apple = pygame.image.load('graphics/apple.png').convert_alpha()
apple = pygame.transform.scale(apple, (cell_size, cell_size))
font = pygame.font.Font('font/CatComic.ttf', 25)

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)

main_game = MAIN()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0,-1)
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != 11:
                    main_game.snake.direction = Vector2(0,1)
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1,0)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1,0)
    
    screen.fill((175,215,70))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)