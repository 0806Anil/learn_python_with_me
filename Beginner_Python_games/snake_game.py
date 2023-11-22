import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Snake parameters
snake_block = 10
snake_speed = 15

# Snake variables
snake = [(width / 2, height / 2)]
snake_direction = (1, 0)

# Food variables
food = (random.randrange(1, width // snake_block) * snake_block,
        random.randrange(1, height // snake_block) * snake_block)

# Main game loop
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and snake_direction != (0, 1):
        snake_direction = (0, -1)
    elif keys[pygame.K_DOWN] and snake_direction != (0, -1):
        snake_direction = (0, 1)
    elif keys[pygame.K_LEFT] and snake_direction != (1, 0):
        snake_direction = (-1, 0)
    elif keys[pygame.K_RIGHT] and snake_direction != (-1, 0):
        snake_direction = (1, 0)

    # Move the snake
    x, y = snake[0]
    x += snake_direction[0] * snake_block
    y += snake_direction[1] * snake_block
    snake.insert(0, (x, y))

    # Check for collisions with boundaries
    if x < 0 or x >= width or y < 0 or y >= height:
        pygame.quit()
        sys.exit()

    # Check if snake eats food
    if x == food[0] and y == food[1]:
        food = (random.randrange(1, width // snake_block) * snake_block,
                random.randrange(1, height // snake_block) * snake_block)
    else:
        snake.pop()

    # Draw the background
    screen.fill(white)

    # Draw the snake
    for segment in snake:
        pygame.draw.rect(screen, black, (segment[0], segment[1], snake_block, snake_block))

    # Draw the food
    pygame.draw.rect(screen, red, (food[0], food[1], snake_block, snake_block))

    # Update the display
    pygame.display.flip()

    # Set the game speed
    clock.tick(snake_speed)
