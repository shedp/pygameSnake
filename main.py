import pygame, sys, random
from pygame.math import Vector2

class FRUIT:
    #create an x & y position
    #draw a square
    def __init__(self):
        self.x = random.randint(0,cell_number-1)
        self.y = random.randint(0,cell_number-1)
        #use vectors to store x,y
        self.pos = Vector2(self.x,self.y)
    
    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.pos.x*cell_size,self.pos.y*cell_size,cell_size,cell_size)
        pygame.draw.rect(screen,(255, 32, 78),fruit_rect)

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(6,10),Vector2(7,10)]
    
    def draw_snake(self):
        for block in self.body:
            #create rect
            #draw rect
            snake_rect = pygame.Rect(block.x*cell_size,block.y*cell_size,cell_size,cell_size)
            pygame.draw.rect(screen,(55, 140, 231),snake_rect)

pygame.init()

cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_size * cell_number, cell_size * cell_number))
pygame.display.set_caption('Snake')
clock = pygame.time.Clock()

fruit = FRUIT()
snake = SNAKE()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill((175,215,70))
    fruit.draw_fruit()
    snake.draw_snake()
    pygame.display.update()
    clock.tick(60)