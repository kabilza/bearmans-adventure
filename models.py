import arcade.key, time, random, arcade.sound


MOVEMENT_SPEED = 4
DIR_STILL = 0
DIR_UP = 1
DIR_RIGHT = 2
DIR_DOWN = 3
DIR_LEFT = 4

MOVEMENT_SPEED = 5
JUMP_SPEED = 18
GRAVITY = -0.5
IS_ALIVE = True

MENU = ["START", "HOW_TO_PLAY", "MAIN"]

n3 = random.randrange(0,100,25)



class Bear:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.direction = DIR_STILL
        self.die = 1
        self.jumpcount = False

        self.next_direction = DIR_STILL

    def jump(self):
        self.jumpcount = True
        self.vy = JUMP_SPEED

    def update(self, delta):
        if self.x < 0:
            self.x = 1440
        elif self.x > 1440:
            self.x = 0
        self.x += self.vx
        if self.y < 0:
            self.die =  1
        if self.y > 900:
            self.y = 900
        
        if self.jumpcount:
            self.y += self.vy
            self.vy += GRAVITY
             
            if self.world.check_bear_on_plat():
                self.vy = 0
        else:
            if not self.world.check_bear_on_plat():
                self.vy = 0

    def on_key_press(self, key, key_modifier):
        if self.die:
            self.world.lives -= 1
            self.die = 0
            if self.world.lives == -2:
                self.world.lives = 6
                self.world.time = 0
            self.world.session += 1
            self.x = 60
            self.y = 200
        if key == arcade.key.RIGHT:
            self.vx = 10
        if key == arcade.key.LEFT:
            self.vx = -10
        if key == arcade.key.UP:
            self.jump()
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


class Enemy:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
    def update(self, delta):
        if self.check_enemy():
            self.world.bear.die = 1
        else:
            self.x = self.x
            self.y = self.y
    
    def hit_bear(self):
        if self.x-45 <= self.world.bear.x <= self.x+45:
            if self.y-60 <= self.world.bear.y <= self.y+60:
                return True
        else:
            return False

class Diamond:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.pow = 1
    def update(self, delta):
        self.x = self.x
        self.y = self.y
    
    def hit_bear2(self):
        if self.x-60 <= self.world.bear.x <= self.x+60:
            if self.y-60 <= self.world.bear.y <= self.y+60:
                return True
        else:
            return False

class Wasp:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
    def update(self, delta):
        if self.check_enemy():
            self.world.bear.die = 1
        else:
            self.x = self.x
            self.y = self.y
    def hit_bear3(self):
        if self.x-42 <= self.world.bear.x <= self.x+42:
            if self.y-40 <= self.world.bear.y <= self.y+40:
                return True
        else:
            return False

class MenuStart:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
    def update(self, delta):
        self.x = self.x
        self.y = self.y
    def on_key_press(self, key, key_modifier):
        if key == arcade.key.ENTER:
            self.world.start1 = MENU[0]
        if key == arcade.key.DOWN:
            self.world.start1 = MENU[1]

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.bear = Bear(self, 60, 175)
        self.platform = []
        self.enemy = []
        self.diamond = []
        self.menulist = []
        self.wasp = []
        self.time = 0
        self.session = 0
        self.lives = 9
        self.start1 = MENU[2]
        self.getlife = 0
        
        self.menulist.append(MenuStart(self, 720,350))

        self.platform.append(Platform(self, 0, 100))
        self.platform.append(Platform(self, 607, 100))
        self.platform.append(Platform(self, 1214, 100))
        self.platform.append(Platform(self, 1800, 100))

        
    def build_plat(self):
        n1 = random.randrange(-300,2048,430)
        n2 = random.randrange(550,1024,179)
        if n1 == self.platform[-1].x:
            n1 += 200
        self.platform.append(Platform(self, n1, n2))
        self.enemy.append(Enemy(self, n1+n3, n2+53))
        self.wasp.append(Wasp(self, n1+n2, n2+n3))
    
    def check_bear_on_plat(self):
        check_list = []
        for p in self.platform:
            check_list.append(p.check_platform())
        return True in check_list

    def ene_on_bear(self):
        cl = []
        for ene in self.enemy:
            cl.append(ene.hit_bear())
        return True in cl

    def diamond_on_bear(self):
        cl3 = []
        for dia in self.diamond:
            cl3.append(dia.hit_bear2())
        return True in cl3

    def wasp_on_bear(self):
        cl4 = []
        for wasp in self.wasp:
            cl4.append(wasp.hit_bear3())
        return True in cl4
    
    def on_key_press(self,key,key_modifier):
        self.bear.on_key_press(key,key_modifier)
        self.menulist[0].on_key_press(key,key_modifier)

    def on_key_release(self,key,key_modifier):
        if self.bear.die == 1:
            self.bear.die = 0
        self.bear.on_key_release(key,key_modifier)
        
    def update(self, delta):
        self.bear.update(delta)
        self.bear.x

        if self.platform[-1].y <= 0:
            for i in range(0,11,1):
                self.build_plat()

            self.diamond.append(Diamond(self, (random.randrange(50,750,330)), (random.randrange(400,800,179))))

            for i in range(5,17,1):
                self.platform.pop(i)
                
        
        if len(self.enemy) > 23:
            for i in range(0,11,1):
                self.enemy.pop(i)

        if len(self.wasp) > 23:
            for i in range(0,12,1):
                self.wasp.pop(i)

        while len(self.platform) < 45:
            self.build_plat()
            self.enemy.pop(0)

        for i in range(4,len(self.platform)):
            self.platform[i].y -= 2
        
        for i in range(len(self.enemy)):
            self.enemy[i].y -= 2

        for i in range(len(self.wasp)):
            self.wasp[i].y -= 4
        
        if self.ene_on_bear():
            self.bear.die = 1
            self.getlife = 0

        if self.wasp_on_bear():
            self.bear.die = 1
            self.getlife = 0

        if self.diamond_on_bear():
            self.time += 10
            self.diamond.pop(0)
            self.getlife += 1

        if self.getlife >= 5:
            self.lives += 1
            self.getlife = 0

        if len(self.diamond) == 3:
            self.bear.die = 1
            self.diamond.clear()
            
        
            
            

