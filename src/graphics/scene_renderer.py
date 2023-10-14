class SceneRenderer:
    def __init__(self, engine):
        self.engine = engine
        self.ctx = engine.ctx
        self.mesh = engine.mesh
        self.scene = engine.scene
        # depth buffer
        self.depth_texture = self.mesh.texture.textures["depth_texture"]
        self.depth_fbo = self.ctx.framebuffer(depth_attachment=self.depth_texture)

    def render_shadow(self):
        self.depth_fbo.clear()
        self.depth_fbo.use()
        for obj in self.scene.objects:
            obj.render_shadow()

    def main_render(self):
        self.engine.ctx.screen.use()
        for obj in self.scene.objects:
            obj.render()
        # self.scene.skybox.render()

    def render(self):
        self.scene.update()
        # pass 1
        self.render_shadow()
        # pass 2
        self.main_render()

    def destroy(self):
        self.depth_fbo.release()
