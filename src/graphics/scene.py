from .model import *
import glm


class Scene:
    def __init__(self, engine):
        self.engine = engine
        self.objects = []
        self.load()
        # skybox
        # self.skybox = AdvancedSkyBox(engine)

    def add_object(self, obj):
        self.objects.append(obj)

    def load(self):
        engine = self.engine
        add = self.add_object

        # floor
        n, s = 20, 2
        for x in range(-n, n, s):
            for z in range(-n, n, s):
                add(Cube(engine, pos=(x, -s, z)))

        # columns
        for i in range(9):
            add(Cube(engine, pos=(15, i * s, -9 + i), tex_id=2))
            add(Cube(engine, pos=(15, i * s, 5 - i), tex_id=2))

        # cat
        add(Cat(engine, pos=(0, -1, -10)))

        # moving cube
        self.moving_cube = MovingCube(engine, pos=(0, 6, 8), scale=(3, 3, 3), tex_id=1)
        add(self.moving_cube)

    def update(self):
        self.moving_cube.rot.xyz = self.engine.time
