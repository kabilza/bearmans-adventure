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
        self.vx = 0
        self.vy = 0
        self.direction = DIR_STILL

        self.next_direction = DIR_STILL


    def update(self, delta):
        self.x += self.vx
        self.y += self.vy

    def on_key_press(self, key, key_modifier):
        if key == arcade.key.RIGHT:
            self.vx = 5
        if key == arcade.key.LEFT:
            self.vx = -5
        if key == arcade.key.UP:
            self.vy = 5  
        if key == arcade.key.DOWN:
            self.vy = -5 

    def on_key_release(self,key,key_modifier):
        if key == arcade.key.RIGHT:
            self.vx = 0
        if key == arcade.key.LEFT:
            self.vx = 0
        if key == arcade.key.UP:
            self.vy = 0
        if key == arcade.key.DOWN:
            self.vy = 0
        

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.bear = Bear(self, 60, 100)
    
    def on_key_press(self,key,key_modifier):
        self.bear.on_key_press(key,key_modifier)

    def on_key_release(self,key,key_modifier):
        self.bear.on_key_release(key,key_modifier)
        
    def update(self, delta):
        self.bear.update(delta)