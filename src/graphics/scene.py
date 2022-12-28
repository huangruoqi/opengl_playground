from .model import *
import glm


class Scene:
    def __init__(self, engine):
        self.engine = engine
        self.objects = []
        self.load()

    def add_object(self, obj):
        self.objects.append(obj)

    def load(self):
        pass

    def update(self):
        pass
