import arcade.key

MOVEMENT_SPEED = 4
DIR_STILL = 0
DIR_UP = 1
DIR_RIGHT = 2
DIR_DOWN = 3
DIR_LEFT = 4

DIR_OFFSETS = {DIR_STILL: (0, 0),
               DIR_UP: (0, 1),
               DIR_RIGHT: (1, 0),
               DIR_DOWN: (0, -1),
               DIR_LEFT: (-1, 0)}

KEY_MAP = { arcade.key.UP: DIR_UP,
            arcade.key.DOWN: DIR_DOWN,
            arcade.key.LEFT: DIR_LEFT,
            arcade.key.RIGHT: DIR_RIGHT, }

class Bear:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.direction = DIR_STILL

    def move(self, direction):
        self.x += MOVEMENT_SPEED * DIR_OFFSETS[direction][0]
        self.y += MOVEMENT_SPEED * DIR_OFFSETS[direction][1]

    def update(self, delta):
        self.move(self.direction)

    def on_key_press(self,key,key_modifier):
        if key in KEY_MAP:
            self.next_direction = KEY_MAP[key]

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.bear = Bear(self, 60, 100)
    
    def on_key_press(self,key,key_modifier):
        self.bear.on_key_press(key,key_modifier)
        
    def update(self, delta):
        self.bear.update(delta)