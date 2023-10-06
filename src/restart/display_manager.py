import pygame
from .mesh import Background



class DisplayManager:
    def __init__(self, engine):
        self.engine = engine
        self.context = engine.context
        self.background = Background(self.context)
        self.font = pygame.font.SysFont(None, 36)
    
    def display_fps(self):
        text_surface = self.font.render(f"{int(1000/self.engine.delta_time)}", True, (0, 0, 0))
        self.background.blit(text_surface, (1880, 1040, text_surface.get_width(), text_surface.get_height()))
        self.background.render()

    def render(self):
        self.context.clear(color=(0.08, 0.16, 0.18))
        self.display_fps()
        

