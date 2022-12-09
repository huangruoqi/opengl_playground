import pygame as pg
import moderngl as mgl
import sys
from .models import *

class GraphicsEngine:
    def __init__(self, win_size=(1600, 900)):
        # init pygame modules
        pg.init()
        # window size
        self.WIN_SIZE = win_size
        # set opengl attributes
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
        # create opengl context
        pg.display.set_mode(self.WIN_SIZE, flags=pg.OPENGL | pg.DOUBLEBUF)
        # detect and use existing opengl cotext
        self.ctx = mgl.create_context()
        # time
        self.clock = pg.time.Clock()
        # create scene
        self.scene = Triangle(self)
        
    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.scene.destroy()
                pg.quit()
                sys.exit()
        
    def render(self):
        # clear framebuffer
        self.ctx.clear(color=(0.08,0.16,0.18))
        # render scene
        self.scene.render()
        # swap buffers
        pg.display.flip()

    def run(self):
        while 1:
            self.check_events()
            self.render()
            self.clock.tick(60)
