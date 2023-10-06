import numpy as np
import moderngl
import pygame
from abc import ABC, abstractclassmethod
from .utils import load_shaders

class Mesh(ABC):
    def __init__(self):
        self.vaos = []

    def render(self):
        [vao.render(moderngl.TRIANGLE_STRIP) for vao in self.vaos]

class Background(Mesh):
    def __init__(self, ctx: moderngl.Context):
        super(Background, self).__init__()
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
        self.vaos.append(ctx.simple_vertex_array(program, vbo, 'vert', 'uv'))

    def blit(self, surface: pygame.Surface, rect: pygame.Rect):
        text_data: bytes = pygame.image.tostring(surface, "RGBA", True)
        self.texture.write(text_data, viewport=tuple(rect))