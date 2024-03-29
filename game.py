import pygame
import time
import random

pygame.init()

#  display
width, height = 1000, 600
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)

# Snake size
snake_block = 10
snake_speed = 10

#first step
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
direction = 'RIGHT'

food_pos = [random.randrange(1, (width//snake_block)) * snake_block,
            random.randrange(1, (height//snake_block)) * snake_block]

#score
score = 0

game_over = False

# Clock to control snake speed
clock = pygame.time.Clock()

#draw the snake
def our_snake(snake_block, snake_list):
    for block in snake_list:
        pygame.draw.rect(display, green, [block[0], block[1], snake_block, snake_block])

#game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                direction = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                direction = 'DOWN'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                direction = 'RIGHT'

    # Move the snake
    if direction == 'UP':
        snake_pos[1] -= snake_block
    elif direction == 'DOWN':
        snake_pos[1] += snake_block
    elif direction == 'LEFT':
        snake_pos[0] -= snake_block
    elif direction == 'RIGHT':
        snake_pos[0] += snake_block

    # Check for collisions with walls or itself
    if snake_pos[0] >= width or snake_pos[0] < 0 or snake_pos[1] >= height or snake_pos[1] < 0:
        game_over = True

    for block in snake_body[1:]:
        if snake_pos == block:
            game_over = True

    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        food_pos = [random.randrange(1, (width//snake_block)) * snake_block,
                    random.randrange(1, (height//snake_block)) * snake_block]
        score += 1
    else:
        snake_body.pop()

    # Update snake body
    snake_body.insert(0, list(snake_pos))

    # Set background color
    display.fill(black)

    # food
    pygame.draw.rect(display, red, [food_pos[0], food_pos[1], snake_block, snake_block])

    # Draw the snake
    our_snake(snake_block, snake_body)

    # score
    font = pygame.font.SysFont(None, 35)
    score_display = font.render("Score: " + str(score), True, white)
    display.blit(score_display, (10, 10))

    # the display
    pygame.display.update()

    # snake speed
    clock.tick(snake_speed)

# Quit the game
pygame.quit()
