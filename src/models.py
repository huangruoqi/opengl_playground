import numpy as np

class Triangle:
    def __init__(self, app):
        self.app = app
        self.ctx = app.ctx
        self.vbo = self.get_vbo()
        self.shader_program = self.get_shader_program('default')
        self.vao = self.get_vao()

    def render(self):
        self.vao.render()

    def destroy(self):
        self.vbo.release()
        self.shader_program.release()
        self.vao.release()


    def get_vertex_data(self):
        vertex_data = [
            ( 1.0,  0.0,  0.0),
            ( 0.0,  1.0,  0.0),
            ( 0.0, -1.0,  0.0),
        ]
        return np.array(vertex_data, dtype='f4')

    def get_vbo(self):
        vertex_data = self.get_vertex_data()
        vbo = self.ctx.buffer(vertex_data)
        return vbo

    def get_vbo_color(self):
        color_data = [
            ( 1.0,  0.0,  0.0),
            ( 0.0,  1.0,  0.0),
            ( 0.0,  0.0,  1.0),
        ]
        vbo = self.ctx.buffer(np.array(color_data, dtype='f4'))
        return vbo

    def get_vao(self):
        color = self.get_vbo_color()
        vao = self.ctx.vertex_array(self.shader_program, [
            (self.vbo, '3f', 'in_position'),
            (color, '3f', 'in_color'),
        ])
        return vao

    def get_shader_program(self, shader_name):
        with open(f'src/shaders/{shader_name}.vert') as file:
            vs = file.read()
        with open(f'src/shaders/{shader_name}.frag') as file:
            fs = file.read()

        program = self.ctx.program(vertex_shader=vs, fragment_shader=fs)
        return program