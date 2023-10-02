import numpy as np
import pygame
import moderngl

class DisplayManager:
    def __init__(self, engine):
        self.engine = engine
        self.context = engine.context
    
    def display_fps(self):
        font = pygame.font.SysFont(None, 36)
        text_surface = font.render(f"{1000/self.engine.delta_time:.1f}", True, (0, 0, 0))
        texture_data = pygame.image.tostring(text_surface, "RGBA", True)
        width, height = text_surface.get_size()

        # Create a texture in ModernGL
        texture = self.context.texture((width, height), 4, texture_data)
        texture.build_mipmaps()

        # Simple shaders
        vertex_shader = """
        #version 330
        in vec2 vert;
        in vec2 uv;
        out vec2 frag_uv;
        void main() {
            gl_Position = vec4(vert, 0.0, 1.0);
            frag_uv = uv;
        }
        """

        fragment_shader = """
        #version 330
        uniform sampler2D tex;
        in vec2 frag_uv;
        out vec4 color;
        void main() {
            color = texture(tex, frag_uv);
        }
        """

        program = self.context.program(vertex_shader=vertex_shader, fragment_shader=fragment_shader)
        program['tex'].value = 0

        # Quad vertices & uvs
        quad = np.array([
            0.85, 0.88, 0.0, 0.0,
            0.95, 0.88, 1.0, 0.0,
            0.85, 0.95, 0.0, 1.0,
            0.95, 0.95, 1.0, 1.0,
        ], dtype='f4')

        vbo = self.context.buffer(quad.tobytes())
        vao = self.context.simple_vertex_array(program, vbo, 'vert', 'uv')
        texture.use()
        vao.render(moderngl.TRIANGLE_STRIP)

    def render(self):
        self.context.clear(color=(0.08, 0.16, 0.18))
        self.display_fps()
