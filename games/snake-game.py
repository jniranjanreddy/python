import pygame
import time

# Initialize the game...
# Initialize the game...
pygame.init()

# Set up the display
width, height = 800, 600
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Set up colors
black = (0, 0, 0)
white = (255, 255, 255)

# Set up the snake
snake_block = 10
snake_speed = 30

x1 = width / 2
y1 = height / 2

x1_change = 0
y1_change = 0

clock = pygame.time.Clock()

game_over = False

while not game_over:
 for event in pygame.event.get():
  if event.type == pygame.QUIT:
   game_over = True
  if event.type == pygame.KEYDOWN:
   if event.key == pygame.K_LEFT:
    x1_change = -snake_block
    y1_change = 0
   elif event.key == pygame.K_RIGHT:
    x1_change = snake_block
    y1_change = 0
   elif event.key == pygame.K_UP:
    y1_change = -snake_block
    x1_change = 0
   elif event.key == pygame.K_DOWN:
    y1_change = snake_block
    x1_change = 0

 if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
  game_over = True

 x1 += x1_change
 y1 += y1_change
 display.fill(black)
 pygame.draw.rect(display, white, [x1, y1, snake_block, snake_block])
 pygame.display.update()
 clock.tick(snake_speed)

pygame.quit()