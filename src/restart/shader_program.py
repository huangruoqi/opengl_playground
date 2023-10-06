from .utils import load_shaders


class ShaderProgram:
    programs = {}
    context = None

    @classmethod
    def register(cls, context):
        cls.context = context

    @classmethod
    def get(cls, name):
        program = cls.programs.get(name)
        if program is None:
            cls.programs[name] = cls.context.program(**load_shaders(name))
            program = cls.programs[name]
        return program

    @classmethod
    def destroy(cls):
        [program.release() for program in cls.programs.values()]
