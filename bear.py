from models import Bear, World

import arcade

SCREEN_WIDTH = 2048
SCREEN_HEIGHT = 1152

SPRITE_SCALING = 1

MOVEMENT_SPEED = 5
JUMP_SPEED = 14
GRAVITY = 1
#1


class BearSprite:
    def __init__(self):
        self.sprite = arcade.Sprite('images/BearSprite1.png',scale = SPRITE_SCALING)
    def draw(self,x,y):
        self.sprite.set_position(x,y)
        self.sprite.draw()


class PlatformSprite:
    def __init__(self):
        self.sprite = arcade.Sprite('images/Platform6.png', scale = 1)
    def draw(self,x,y):
        self.sprite.set_position(x,y)
        self.sprite.draw()

class EnemySprite:
    def __init__(self):
        self.sprite = arcade.Sprite('images/enemy1.png',scale = SPRITE_SCALING)
    def draw(self,x,y):
        self.sprite.set_position(x,y)
        self.sprite.draw()

class DiamondSprite:
    def __init__(self):
        self.sprite = arcade.Sprite('images/diamond.png',scale = SPRITE_SCALING)
    def draw(self,x,y):
        self.sprite.set_position(x,y)
        self.sprite.draw()   


class BearWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height, "Bear's Adventure")

        self.platform_sprite = arcade.SpriteList
        self.game_over = False

        self.bear_sprite = BearSprite()
        self.bear_sprite.center_x = SCREEN_WIDTH - 180
        self.bear_sprite.center_y = SCREEN_HEIGHT - 1000

        self.platform_sprite = PlatformSprite()
        self.platform_sprite.center_x = SCREEN_WIDTH - 100
        self.platform_sprite.center_y = SCREEN_HEIGHT - 100

        self.enemy_sprite = EnemySprite()
        self.enemy_sprite.center_x = SCREEN_WIDTH - 100
        self.enemy_sprite.center_y = SCREEN_HEIGHT - 100

        self.diamond_sprite = DiamondSprite()
        self.diamond_sprite.center_x = SCREEN_WIDTH - 100
        self.diamond_sprite.center_y = SCREEN_HEIGHT - 100

        self.background = arcade.load_texture("images/BG.png")
        self.world = World(width,height)
        arcade.set_background_color(arcade.color.SILVER)

    def draw_plat(self):
        for i in self.world.platform:
            self.platform_sprite.draw(i.x,i.y)

    def draw_enemy(self):
        for i in self.world.enemy:
            self.enemy_sprite.draw(i.x,i.y)

    def draw_diamond(self):
        for i in self.world.diamond:
            self.diamond_sprite.draw(i.x,i.y)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)


        start_x = 100
        start_y = 1100
        arcade.draw_text(f"Survival Time: {int(self.world.time)//60}:{int(self.world.time)%60:.1f}", start_x, start_y, arcade.color.BLACK, 30)
        arcade.draw_text(f"Bearman's Adventure", 1650, 1100, arcade.color.BLACK, 30)
        arcade.draw_text(f"Lives : {self.world.lives + 2}", 600, 1100, arcade.color.BLACK, 30)
        arcade.draw_text(f"High Score : {self.world.highscore}", 900, 1100, arcade.color.BLACK, 30)



        

        self.bear_sprite.draw(self.world.bear.x,self.world.bear.y)

        self.draw_plat()   
        self.draw_enemy()
        self.draw_diamond()

        if self.world.bear.die == 1:
            if self.world.session != 0:
                arcade.draw_text(f"You survived for {int(self.world.time)//60}:{int(self.world.time)%60:.1f}!!!", 553, 700, arcade.color.BLACK, 60)
                arcade.draw_text(f"You survived for {int(self.world.time)//60}:{int(self.world.time)%60:.1f}!!!", 553, 700, arcade.color.YELLOW, 59)
                arcade.draw_text(f"GAME OVER!!!", 553, 600, arcade.color.BLACK, 60)
                arcade.draw_text(f"GAME OVER!!!", 551, 600, arcade.color.WHITE, 59)
                if self.world.lives == -2:
                    self.world.highscore = int(self.world.time)
                    self.world.lives = 6
                    
                

            arcade.draw_text(f"Press any key to START!!!", 553, 500, arcade.color.BLACK, 60)
            arcade.draw_text(f"Press any key to START!!!", 551, 500, arcade.color.WHITE, 59)


    def on_key_press(self,key,key_modifier):
        self.world.on_key_press(key,key_modifier)

    def on_key_release(self,key,key_modifier):
        self.world.on_key_release(key,key_modifier)

    def update(self, delta):
        if self.world.bear.die == 1:
            return
        self.world.update(delta)
        self.world.time += delta
        if self.world.lives == -2:
            self.world.highscore = int(self.world.time)

        

def main():
    window = BearWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.set_window(window)
    window.world.build_plat()
    arcade.run()



if __name__ == '__main__':
    main()



