import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Advanced Pong")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# Paddle parameters
paddle_width, paddle_height = 10, 60
player_paddle_x, player_paddle_y = 10, height // 2 - paddle_height // 2
opponent_paddle_x, opponent_paddle_y = width - 20, height // 2 - paddle_height // 2
paddle_speed = 10

# Ball parameters
ball_size = 10
ball_speed = 3
ball_direction = [random.choice([-1, 1]), random.choice([-1, 1])]
ball_position = [width // 2 - ball_size // 2, height // 2 - ball_size // 2]

# Score variables
player_score = 0
opponent_score = 0
font = pygame.font.SysFont(None, 35)

# Function to reset the ball
def reset_ball():
    return [width // 2 - ball_size // 2, height // 2 - ball_size // 2]

# Main game loop
clock = pygame.time.Clock()
running = True
paused = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused
            elif event.key == pygame.K_q:
                running = False

    if not paused:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and player_paddle_y > 0:
            player_paddle_y -= paddle_speed
        if keys[pygame.K_DOWN] and player_paddle_y < height - paddle_height:
            player_paddle_y += paddle_speed

        # Move the opponent paddle
        if opponent_paddle_y + paddle_height // 2 < ball_position[1]:
            opponent_paddle_y += paddle_speed
        elif opponent_paddle_y + paddle_height // 2 > ball_position[1]:
            opponent_paddle_y -= paddle_speed

        # Move the ball
        ball_position[0] += ball_speed * ball_direction[0]
        ball_position[1] += ball_speed * ball_direction[1]

        # Ball collisions with walls
        if ball_position[1] <= 0 or ball_position[1] >= height - ball_size:
            ball_direction[1] *= -1

        # Ball collisions with paddles
        if (
            player_paddle_x <= ball_position[0] <= player_paddle_x + paddle_width
            and player_paddle_y <= ball_position[1] <= player_paddle_y + paddle_height
        ):
            ball_direction[0] *= -1
        elif (
            opponent_paddle_x - ball_size <= ball_position[0] <= opponent_paddle_x
            and opponent_paddle_y <= ball_position[1] <= opponent_paddle_y + paddle_height
        ):
            ball_direction[0] *= -1

        # Check for scoring
        if ball_position[0] < 0:
            opponent_score += 1
            ball_position = reset_ball()
        elif ball_position[0] > width:
            player_score += 1
            ball_position = reset_ball()

    # Draw background
    screen.fill(black)

    # Draw paddles
    pygame.draw.rect(screen, white, (player_paddle_x, player_paddle_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, white, (opponent_paddle_x - paddle_width, opponent_paddle_y, paddle_width, paddle_height))

    # Draw ball
    pygame.draw.rect(screen, white, (ball_position[0], ball_position[1], ball_size, ball_size))

    # Display scores
    player_score_text = font.render("Player: " + str(player_score), True, white)
    opponent_score_text = font.render("Opponent: " + str(opponent_score), True, white)
    screen.blit(player_score_text, (width // 4, 10))
    screen.blit(opponent_score_text, (width // 2, 10))

    # Display pause message
    if paused:
        pause_text = font.render("Paused", True, white)
        screen.blit(pause_text, (width // 2 - 50, height // 2 - 20))

    # Update the display
    pygame.display.flip()

    # Set the game speed
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
