import arcade.key

class Bear:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y

    def on_draw(self):
        self.set_position(self.x, self..y)

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.bear = Bear(self, 60, 100)