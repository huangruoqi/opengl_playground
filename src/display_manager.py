from .mesh.ui import UI


class DisplayManager:
    def __init__(self, engine):
        self.engine = engine
        self.context = engine.context
        self.ui = UI(self.context, *self.engine.WIN_SIZE)

    def update(self):
        self.ui.update_fps(int(1000/self.engine.delta_time))

    def render(self):
        self.context.clear(color=(0.08, 0.16, 0.18))
        self.ui.render()
