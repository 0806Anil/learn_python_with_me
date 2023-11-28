import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ping Pong Game")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# Paddle parameters
paddle_width, paddle_height = 15, 100
left_paddle_x, right_paddle_x = 50, width - 50 - paddle_width
left_paddle_y, right_paddle_y = height // 2 - paddle_height // 2, height // 2 - paddle_height // 2
paddle_speed = 10

# Ball parameters
ball_size = 20
ball_x, ball_y = width // 2 - ball_size // 2, height // 2 - ball_size // 2
ball_speed_x, ball_speed_y = 5, 5

# Game state
is_paused = False

# Main game loop
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                is_paused = not is_paused

    if not is_paused:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and left_paddle_y > 0:
            left_paddle_y -= paddle_speed
        if keys[pygame.K_s] and left_paddle_y < height - paddle_height:
            left_paddle_y += paddle_speed
        if keys[pygame.K_UP] and right_paddle_y > 0:
            right_paddle_y -= paddle_speed
        if keys[pygame.K_DOWN] and right_paddle_y < height - paddle_height:
            right_paddle_y += paddle_speed

        # Move the ball
        ball_x += ball_speed_x
        ball_y += ball_speed_y

        # Ball collision with paddles
        if (
            left_paddle_x < ball_x < left_paddle_x + paddle_width
            and left_paddle_y < ball_y < left_paddle_y + paddle_height
        ) or (
            right_paddle_x < ball_x + ball_size < right_paddle_x + paddle_width
            and right_paddle_y < ball_y < right_paddle_y + paddle_height
        ):
            ball_speed_x *= -1

        # Ball collision with walls
        if ball_y < 0 or ball_y > height - ball_size:
            ball_speed_y *= -1

        # Ball out of bounds
        if ball_x < 0 or ball_x > width:
            ball_x, ball_y = width // 2 - ball_size // 2, height // 2 - ball_size // 2
            ball_speed_x *= -1

        # Draw background
        screen.fill(black)

        # Draw paddles
        pygame.draw.rect(screen, white, (left_paddle_x, left_paddle_y, paddle_width, paddle_height))
        pygame.draw.rect(screen, white, (right_paddle_x, right_paddle_y, paddle_width, paddle_height))

        # Draw ball
        pygame.draw.ellipse(screen, white, (ball_x, ball_y, ball_size, ball_size))

    else:
        # Draw pause screen
        pygame.draw.rect(screen, white, (width // 2 - 50, height // 2 - 25, 100, 50))
        font = pygame.font.SysFont(None, 35)
        text = font.render("Paused", True, black)
        screen.blit(text, (width // 2 - 35, height // 2 - 15))

    # Update the display
    pygame.display.flip()

    # Set the game speed
    clock.tick(60)
