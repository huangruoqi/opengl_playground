import moderngl
from .utils import load_shaders, SingletonFieldClass


class Mesh(SingletonFieldClass):
    def __init__(self, *args, **kwargs):
        super(Mesh, self).__init__(*args, **kwargs)

    def render(self):
        self.vao.render(moderngl.TRIANGLE_STRIP)

    @classmethod
    def get_program(cls, ctx: moderngl.Context, name: str):
        return ctx.program(**load_shaders(name))

