from models import Bear, World

import arcade

SCREEN_WIDTH = 2048
SCREEN_HEIGHT = 1152

SPRITE_SCALING = 1.5

class BearSprite:
    def __init__(self):
        self.sprite = arcade.Sprite('images/BearSprite1.png',scale = SPRITE_SCALING)
    def draw(self,x,y):
        self.sprite.set_position(x,y)
        self.sprite.draw()
    


class BearWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        self.bear_sprite = BearSprite()
        self.bear_sprite.center_x = SCREEN_WIDTH - 180
        self.bear_sprite.center_y = SCREEN_HEIGHT - 1000

        self.background = arcade.load_texture("images/BG.png")
        self.world = World(width,height)
        arcade.set_background_color(arcade.color.SILVER)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

        self.bear_sprite.draw(self.world.bear.x,self.world.bear.y)

    def on_key_press(self,key,key_modifier):
        self.world.on_key_press(key,key_modifier)

    def update(self, delta):
        self.world.update(delta)




def main():
    window = BearWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()


if __name__ == '__main__':
    main()