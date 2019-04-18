import arcade.key, time

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
        if self.x < 0:
            self.x = 0
        elif self.x > 2048:
            self.x = 2048
        self.x += self.vx
        self.y += self.vy

    def on_key_press(self, key, key_modifier):
        if key == arcade.key.RIGHT:
            self.vx = 10
        if key == arcade.key.LEFT:
            self.vx = -10
        if key == arcade.key.UP:
            self.vy = 10
        if key == arcade.key.DOWN:
            self.vy = -10

    def on_key_release(self,key,key_modifier):
        if key == arcade.key.RIGHT:
            self.vx = 0
        if key == arcade.key.LEFT:
            self.vx = 0
        if key == arcade.key.UP:
            self.vy = 0
        if key == arcade.key.DOWN:
            self.vy = 0
        
class Platform:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
    def update(self, delta):
        self.x = self.x
        self.y = self.y

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.bear = Bear(self, 60, 200)
        self.platform = []
        self.time = 0

        #lv1
        self.platform.append(Platform(self, 0, 100))
        self.platform.append(Platform(self, 1208, 100))
        self.platform.append(Platform(self, 2416, 100))

        #lv2
        self.platform.append(Platform(self, 0, 350))
        self.platform.append(Platform(self, 1500, 350))

        #lv3
        self.platform.append(Platform(self, -300, 600))
        self.platform.append(Platform(self, 1350, 600))
        self.platform.append(Platform(self, 2416, 100))

        #lv4
        self.platform.append(Platform(self, -600, 600))
        self.platform.append(Platform(self, 1208, 600))
        self.platform.append(Platform(self, 500, 100))

    
    def on_key_press(self,key,key_modifier):
        self.bear.on_key_press(key,key_modifier)

    def on_key_release(self,key,key_modifier):
        self.bear.on_key_release(key,key_modifier)
        
    def update(self, delta):
        self.bear.update(delta)

        self.platform[3].y -= 1
