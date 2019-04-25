import arcade.key, time, random

MOVEMENT_SPEED = 4
DIR_STILL = 0
DIR_UP = 1
DIR_RIGHT = 2
DIR_DOWN = 3
DIR_LEFT = 4

MOVEMENT_SPEED = 5
JUMP_SPEED = 14
GRAVITY = 12
IS_ALIVE = True

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
        self.die = 1

        self.next_direction = DIR_STILL


    def update(self, delta):
        if self.world.check_enemy_on_plat():
            self.die = 1
        if self.x < 0:
            self.x = 2048
        elif self.x > 2048:
            self.x = 0
        self.x += self.vx
        if self.y < 0:
            self.die =  1
        
        if self.world.check_bear_on_plat():
            self.y += self.vy
        else:
            self.y += self.vy - GRAVITY

    def on_key_press(self, key, key_modifier):
        self.die = 0
        if key == arcade.key.RIGHT:
            self.vx = 10
        if key == arcade.key.LEFT:
            self.vx = -10
        if key == arcade.key.UP:
            self.vy = 25
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
            if self.y - 9 <=self.world.bear.y - 67 <= self.y + 9:
                    return True
        else:
            return False
    def check_enemy(self):
        if self.x - 60 <= self.world.bear.x <= self.x + 60 :
            if self.y - 58 <= self.world.bear.y <= self.y + 58:
                return True
        else:
            return False

class Enemy:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
    def update(self, delta):
        if self.check_enemy():
            self.world.time -= 10
            print("HELP")
            self.world.bear.die = 1
        else:
            self.x = self.x
            self.y = self.y
    def check_enemy(self):
        if self.x - 60 <= self.world.bear.x <= self.x + 60 :
            if self.y - 58 <= self.world.bear.y <= self.y + 58:
                    return True
        else:
            return False

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.bear = Bear(self, 60, 200)
        self.platform = []
        self.enemy = []
        self.time = 0
    
        #lv1
        self.platform.append(Platform(self, 0, 100))
        self.platform.append(Platform(self, 607, 100))
        self.platform.append(Platform(self, 1214, 100))
        self.platform.append(Platform(self, 1800, 100))

        
    def build_plat(self):
        n1 = random.randrange(-300,2048,430)
        n2 = random.randrange(500,1024,179)
        n3 = random.randrange(0,100,25)
        if n1 == self.platform[-1].x:
            n1 += 200
        self.platform.append(Platform(self, n1, n2))
        self.enemy.append(Enemy(self, n1+n3, n2+53))
    
    def check_bear_on_plat(self):
        check_list = []
        for p in self.platform:
            check_list.append(p.check_platform())
        return True in check_list

    def check_enemy_on_plat(self):
        check_list2 = []
        for p in self.platform:
            check_list2.append(p.check_enemy())
        return True in check_list2

    
    def on_key_press(self,key,key_modifier):
        self.bear.on_key_press(key,key_modifier)

    def on_key_release(self,key,key_modifier):
        self.bear.on_key_release(key,key_modifier)
        
    def update(self, delta):
        self.bear.update(delta)
        self.bear.x
        if self.platform[-1].y <= 0:
            self.build_plat()
            self.build_plat()
            self.build_plat()
            self.build_plat()
            self.build_plat()
            self.build_plat()
            self.build_plat()
            self.build_plat()
            self.build_plat()
            self.build_plat()
            self.build_plat()
            self.build_plat()
            self.platform.pop(5)
            self.platform.pop(6)
            self.platform.pop(7)
            self.platform.pop(8)
            self.platform.pop(9)
            self.platform.pop(10)
            self.platform.pop(11)
            self.platform.pop(12)
            self.platform.pop(13)
            self.platform.pop(14)
            self.platform.pop(15)
            self.platform.pop(16)

        if self.enemy[-1].y <= 0:
            self.enemy.pop(0)
            self.enemy.pop(1)
            self.enemy.pop(2)
            self.enemy.pop(3)
            self.enemy.pop(4)
            self.enemy.pop(5)
            self.enemy.pop(6)
            self.enemy.pop(7)
            self.enemy.pop(8)
            self.enemy.pop(9)
            self.enemy.pop(10)
            self.enemy.pop(11)
            self.enemy.pop(12)
            
        while len(self.platform) < 50:
            self.build_plat()
            self.enemy.pop(0)
            

        
        for i in range(4,len(self.platform)):
            self.platform[i].y -= 2
        
        for i in range(len(self.enemy)):
            self.enemy[i].y -= 2
            
            
