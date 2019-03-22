import arcade

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 576

SPRITE_SCALING = 0.75

class ModelSprite(arcade.Sprite):
    def __init__(self, *args, **kwargs):
        self.model = kwargs.pop('model', None)

        super().__init__(*args, **kwargs)

    def sync_with_model(self):
        if self.model:
            self.set_position(self.model.x, self.model.y)

    def draw(self):
        self.sync_with_model()
        super().draw()

class BearWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        self.bear_sprite = ModelSprite('images/BearSprite1.png', scale=SPRITE_SCALING)
        self.bear_sprite.center_x = SCREEN_WIDTH - 90
        self.bear_sprite.center_y = SCREEN_HEIGHT - 500

        self.background = arcade.load_texture("images/BG.png")

        arcade.set_background_color(arcade.color.SILVER)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

        self.bear_sprite.draw()



def main():
    window = BearWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()


if __name__ == '__main__':
    main()
