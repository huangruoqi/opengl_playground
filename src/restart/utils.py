import os


def load_shaders(name):
    vert_path = os.path.join('src', 'shader', f'{name}.vert')
    frag_path = os.path.join('src', 'shader', f'{name}.frag')
    with open(vert_path) as vf, open(frag_path) as ff:
        return {'vertex_shader':vf.read(), 'fragment_shader':ff.read()}