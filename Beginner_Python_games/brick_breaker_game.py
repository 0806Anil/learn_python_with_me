import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Brick Breaker")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Paddle
paddle_width, paddle_height = 100, 10
paddle_x = width // 2 - paddle_width // 2
paddle_y = height - 30
paddle_speed = 10

# Ball
ball_radius = 10
ball_x = width // 2
ball_y = height - 50
ball_speed_x = 5
ball_speed_y = -5

# Bricks
brick_width, brick_height = 80, 20
bricks = []
for i in range(10):
    for j in range(5):
        brick = pygame.Rect(i * (brick_width + 5), j * (brick_height + 5), brick_width, brick_height)
        bricks.append(brick)

# Score
score = 0
font = pygame.font.SysFont(None, 35)

# Game state
is_game_over = False
is_paused = False

def draw_paddle(x, y):
    pygame.draw.rect(screen, white, (x, y, paddle_width, paddle_height))

def draw_ball(x, y):
    pygame.draw.circle(screen, white, (x, y), ball_radius)

def draw_bricks():
    for brick in bricks:
        pygame.draw.rect(screen, white, brick)

def display_score(score):
    score_text = font.render("Score: " + str(score), True, black)
    screen.blit(score_text, (10, 10))

def game_over():
    game_over_text = font.render("Game Over", True, white)
    screen.blit(game_over_text, (width // 2 - 70, height // 2 - 20))

def pause_game():
    pause_text = font.render("Paused", True, white)
    screen.blit(pause_text, (width // 2 - 50, height // 2 - 20))

# Main game loop
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                is_paused = not is_paused
            elif event.key == pygame.K_q:
                pygame.quit()
                sys.exit()

    if not is_game_over and not is_paused:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle_x > 0:
            paddle_x -= paddle_speed
        if keys[pygame.K_RIGHT] and paddle_x < width - paddle_width:
            paddle_x += paddle_speed

        ball_x += ball_speed_x
        ball_y += ball_speed_y

        # Ball and wall collisions
        if ball_x - ball_radius <= 0 or ball_x + ball_radius >= width:
            ball_speed_x *= -1
        if ball_y - ball_radius <= 0:
            ball_speed_y *= -1

        # Paddle collision
        if (
            paddle_x <= ball_x <= paddle_x + paddle_width
            and paddle_y <= ball_y + ball_radius <= paddle_y + paddle_height
        ):
            ball_speed_y *= -1

        # Brick collisions
        for brick in bricks:
            if brick.colliderect(pygame.Rect(ball_x - ball_radius, ball_y - ball_radius, 2 * ball_radius, 2 * ball_radius)):
                bricks.remove(brick)
                score += 1
                ball_speed_y *= -1

        # Check if the ball hits the bottom
        if ball_y + ball_radius >= height:
            is_game_over = True

        # Check if all bricks are destroyed
        if not bricks:
            is_game_over = True

    # Draw background
    screen.fill(black)

    # Draw paddle
    draw_paddle(paddle_x, paddle_y)

    # Draw ball
    draw_ball(ball_x, ball_y)

    # Draw bricks
    draw_bricks()

    # Display score
    display_score(score)

    # Display game over text
    if is_game_over:
        game_over()

    # Display pause text
    if is_paused and not is_game_over:
        pause_game()

    # Update the display
    pygame.display.flip()

    # Set the game speed
    clock.tick(60)
