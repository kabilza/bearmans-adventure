import arcade.key, time, random

MOVEMENT_SPEED = 4
DIR_STILL = 0
DIR_UP = 1
DIR_RIGHT = 2
DIR_DOWN = 3
DIR_LEFT = 4

MOVEMENT_SPEED = 5
JUMP_SPEED = 14
GRAVITY = 2

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
            self.x = 2048
        elif self.x > 2048:
            self.x = 0
        self.x += self.vx
        if self.world.check_bear_on_plat():
            self.y += self.vy
        else:
            self.y += self.vy - GRAVITY

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
    def check_platform(self):
        if self.x - 266 <= self.world.bear.x <= self.x + 266:
            if self.world.bear.y - 67 == self.y + 9:
                    return True
        else:
            return False

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.bear = Bear(self, 60, 200)
        self.platform = []
        self.time = 0
    
        #lv1
        self.platform.append(Platform(self, 0, 100))
        self.platform.append(Platform(self, 607, 100))
        self.platform.append(Platform(self, 1214, 100))
        self.platform.append(Platform(self, 1800, 100))

        for i in range(100):
            n1 =random.randrange(500,2512,179)
            if n1 == self.platform[-1].x:
                n1 += 80
            self.platform.append(Platform(self, random.randrange(-700,2048,430), n1))

        # #lv2
        # self.platform.append(Platform(self, 0, 350))
        # self.platform.append(Platform(self, 1500, 350))

        # #lv3
        # self.platform.append(Platform(self, -300, 600))
        # self.platform.append(Platform(self, 1350, 600))
        # self.platform.append(Platform(self, 2416, 100))

        # #lv4
        # self.platform.append(Platform(self, -600, 600))
        # self.platform.append(Platform(self, 1208, 600))
        # self.platform.append(Platform(self, 500, 100))

    def check_bear_on_plat(self):
        check_list = []
        for p in self.platform:
            check_list.append(p.check_platform())
        return True in check_list

    
    def on_key_press(self,key,key_modifier):
        self.bear.on_key_press(key,key_modifier)

    def on_key_release(self,key,key_modifier):
        self.bear.on_key_release(key,key_modifier)
        
    def update(self, delta):
        self.bear.update(delta)
        self.bear.x

        for i in range(4,len(self.platform)):
            self.platform[i].y -= 1
