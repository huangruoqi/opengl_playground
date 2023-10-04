import moderngl
import pygame
import struct
from pygame.locals import QUIT
from src.restart.utils import load_shaders

# Initialize pygame and moderngl
pygame.init()
window = pygame.display.set_mode((800, 600), pygame.DOUBLEBUF | pygame.OPENGL)
ctx = moderngl.create_context()
ctx.enable(flags=moderngl.BLEND)

# Shader program for text rendering
prog = ctx.program(**load_shaders('text'))

# Load font and create texture
font = pygame.font.Font(None, 36)

# Create an empty texture
texture = ctx.texture((800, 600), 4, dtype='f1')
texture.use(location=0)
prog['tex'].value = 0
vertices = [
    -1.0,  1.0,  0.0, 1.0,
     1.0,  1.0,  1.0, 1.0,
    -1.0, -1.0,  0.0, 0.0,
     1.0, -1.0,  1.0, 0.0
]

# Create a VAO to store buffer data and shader program configuration
vertex_data = struct.pack('16f', *vertices)
buffer = ctx.buffer(data=vertex_data)
vao = ctx.simple_vertex_array(prog, buffer, 'vert', 'uv')
# Shader program for text rendering

# Main loop
running = True
frame_count = 0
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    text = f"Frame: {frame_count}"
    frame_count += 1

    # Render text to a surface
    text_surface = font.render(text, True, (255, 255, 255))
    text_data = pygame.image.tostring(text_surface, "RGBA", True)

    # Update texture data
    texture.write(text_data, viewport=(0, 0, text_surface.get_width(), text_surface.get_height()))

    # Draw
    ctx.clear(0.0, 0.0, 0.0)
    ctx.screen.use()
    vao.render(moderngl.TRIANGLE_STRIP)

    pygame.display.flip()

pygame.quit()
