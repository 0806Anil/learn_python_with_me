import pyglet
import random

# Set up the game window
window = pyglet.window.Window(800, 600, "Dodge the Obstacles")
batch = pyglet.graphics.Batch()

# Score
score_label = pyglet.text.Label("Score: 0", font_name="Arial", font_size=20,
                                 x=10, y=window.height - 30, anchor_x='left', anchor_y='center')

# Player
player = pyglet.shapes.Rectangle(x=window.width // 2 - 20, y=30, width=40, height=40, color=(255, 0, 0))

# Obstacles
obstacles = []

def spawn_obstacle(dt):
    x = random.randint(0, window.width - 40)
    obstacle = pyglet.shapes.Rectangle(x=x, y=window.height, width=40, height=40, color=(0, 0, 255), batch=batch)
    obstacles.append(obstacle)

# Update function
def update(dt):
    global obstacles

    for obstacle in obstacles:
        obstacle.y -= 5
        if obstacle.y < 0:
            obstacles.remove(obstacle)
            update_score(1)

    # Check for collisions
    for obstacle in obstacles:
        if (
            player.x < obstacle.x + obstacle.width and
            player.x + player.width > obstacle.x and
            player.y < obstacle.y + obstacle.height and
            player.y + player.height > obstacle.y
        ):
            pyglet.app.exit()  # Game over

# Update score function
def update_score(points):
    global score_label
    score_label.text = "Score: {}".format(int(score_label.text.split(":")[1]) + points)

# Key handling
keys = pyglet.window.key.KeyStateHandler()
window.push_handlers(keys)

@window.event
def on_draw():
    window.clear()
    batch.draw()
    score_label.draw()
    player.draw()

@window.event
def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.RIGHT and player.x < window.width - player.width:
        player.x += 10
    elif symbol == pyglet.window.key.LEFT and player.x > 0:
        player.x -= 10

# Schedule obstacle spawning
pyglet.clock.schedule_interval(spawn_obstacle, 2.0)
pyglet.clock.schedule_interval(update, 1/60.0)

pyglet.app.run()
