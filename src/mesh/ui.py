import moderngl
import pygame
import numpy as np
from .mesh import Mesh


class UI(Mesh):
    def __init__(self, ctx: moderngl.Context, width: int, height: int):
        super(UI, self).__init__(ctx, width, height)
        self.font = pygame.font.SysFont(None, 36)
        self.fps_arr = []
        self.fps = 0

    def get_fields(self, ctx: moderngl.Context, width: int, height: int):
        fields = {}
        fields["texture"] = ctx.texture((width, height), 4, dtype="f1")
        fields["texture"].use(location=0)
        program = Mesh.get_program(ctx, "simple")
        program["tex"].value = 0
        quad = np.array(
            [
                -1, -1, 0.0, 0.0,
                1, -1, 1.0, 0.0,
                -1, 1, 0.0, 1.0,
                1, 1, 1.0, 1.0,
            ],
            dtype="f4",
        )
        vbo = ctx.buffer((quad).tobytes())
        fields["vao"] = ctx.simple_vertex_array(program, vbo, "vert", "uv")
        return fields

    def blit(self, surface: pygame.Surface, rect: pygame.Rect):
        text_data: bytes = pygame.image.tostring(surface, "RGBA", True)
        self.texture.write(text_data, viewport=tuple(rect))

    def update_fps(self, fps):
        if abs(self.fps - fps) > 5:
            self.fps_arr = [fps]*100
        else:
            self.fps_arr.append(fps)
        if len(self.fps_arr)>=100 :
            self.fps = sum(self.fps_arr)//len(self.fps_arr)
            self.fps_arr.clear()
            text_surface = self.font.render(f"FPS: {self.fps}", True, (0, 0, 0))
            self.blit(
                text_surface,
                (650, 750, text_surface.get_width(), text_surface.get_height()),
            )