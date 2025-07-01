from ursina import *

app = Ursina()

# Create a ground
ground = Entity(model='plane', scale=(10,1,10), texture='white_cube', texture_scale=(10,10), collider='box')

# Create a player cube
player = Entity(model='cube', color=color.orange, scale=1, collider='box')

speed = 5

def update():
    # Movement input
    player.x += (held_keys['d'] - held_keys['a']) * speed * time.dt
    player.z += (held_keys['w'] - held_keys['s']) * speed * time.dt

    # Keep player above the ground
    player.y = 0.5

app.run()
