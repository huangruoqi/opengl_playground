import numpy as np
import pygame as pg
import moderngl
from .utils import load_shaders
import time

class Mesh:
    def __init__(self, ctx):
        font = pg.font.SysFont(None, 36)
        text_surface = font.render(f"{time.time()}", True, (0, 0, 0))
        texture_data = pg.image.tostring(text_surface, "RGBA", True)
        width, height = text_surface.get_size()

        # Create a texture in ModernGL

        self.texture = ctx.texture((1920, 1080), 4, dtype='f1')
        self.texture.use(location=0)

        program = ctx.program(**load_shaders('text'))
        program['tex'].value = 0
        quad = np.array([
            -1, -1, 0.0, 0.0,
            1, -1, 1.0, 0.0,
            -1, 1, 0.0, 1.0,
            1, 1, 1.0, 1.0,
        ], dtype='f4')

        vbo = ctx.buffer((quad).tobytes())

        # Quad vertices & uvs
        self.vao = ctx.simple_vertex_array(program, vbo, 'vert', 'uv')


class DisplayManager:
    def __init__(self, engine):
        self.engine = engine
        self.context = engine.context
        self.mesh = Mesh(self.context)
        self.font = pg.font.SysFont(None, 36)
    
    def display_fps(self):
        for i in range(500):
            text_surface = self.font.render(f"{time.time()}", True, (0, 0, 0))
            text_data = pg.image.tostring(text_surface, "RGBA", True)
            self.mesh.texture.write(text_data, viewport=(0, 0, text_surface.get_width(), text_surface.get_height()))
            self.mesh.vao.render(moderngl.TRIANGLE_STRIP)

    def render(self):
        self.context.clear(color=(0.08, 0.16, 0.18))
        self.display_fps()
        

