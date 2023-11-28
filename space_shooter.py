import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Space Shooter")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Player spaceship
player_size = 40
player_x = width // 2 - player_size // 2
player_y = height - player_size - 10
player_speed = 6

# Bullets
bullet_size = 5
bullet_speed = 5         
bullets = []

# Obstacles
obstacle_size = 20
obstacle_speed = 5
obstacles = []

# Score
score = 0
font = pygame.font.SysFont(None, 35)

def draw_player(x, y):
    pygame.draw.rect(screen, white, (x, y, player_size, player_size))

def draw_bullet(x, y):
    pygame.draw.rect(screen, white, (x, y, bullet_size, bullet_size))

def draw_obstacle(x, y):
    pygame.draw.rect(screen, red, (x, y, obstacle_size, obstacle_size))

def display_score(score):
    score_text = font.render("Score: " + str(score), True, white)
    screen.blit(score_text, (10, 10))

# Main game loop
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < width - player_size:
        player_x += player_speed
    if keys[pygame.K_SPACE]:
        bullets.append([player_x + player_size // 2 - bullet_size // 2, player_y])

    # Move bullets
    for bullet in bullets:
        bullet[1] -= bullet_speed

    # Move obstacles and check for collisions
    for obstacle in obstacles:
        obstacle[1] += obstacle_speed

        if obstacle[1] > height:
            obstacle[1] = 0
            obstacle[0] = random.randint(0, width - obstacle_size)
            score += 1

        # Check for collision with player
        if (
            player_x < obstacle[0] + obstacle_size
            and player_x + player_size > obstacle[0]
            and player_y < obstacle[1] + obstacle_size
            and player_y + player_size > obstacle[1]
        ):
            pygame.quit()
            sys.exit()

        # Check for collision with bullets
        for bullet in bullets:
            if (
                bullet[0] < obstacle[0] + obstacle_size
                and bullet[0] + bullet_size > obstacle[0]
                and bullet[1] < obstacle[1] + obstacle_size
                and bullet[1] + bullet_size > obstacle[1]
            ):
                obstacles.remove(obstacle)
                bullets.remove(bullet)
                obstacle[1] = 0
                obstacle[0] = random.randint(0, width - obstacle_size)
                score += 1

    # Remove bullets that are off-screen
    bullets = [bullet for bullet in bullets if bullet[1] > 0]

    # Add new obstacles
    if random.randint(0, 100) < 5:
        obstacles.append([random.randint(0, width - obstacle_size), 0])

    # Draw background
    screen.fill(black)

    # Draw player spaceship
    draw_player(player_x, player_y)

    # Draw bullets
    for bullet in bullets:
        draw_bullet(bullet[0], bullet[1])

    # Draw obstacles
    for obstacle in obstacles:
        draw_obstacle(obstacle[0], obstacle[1])

    # Display score
    display_score(score)

    # Update the display
    pygame.display.flip()

    # Set the game speed
    clock.tick(30)  
