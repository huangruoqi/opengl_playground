#version 330
in vec2 vert;
in vec2 uv;
out vec2 frag_uv;
void main() {
    gl_Position = vec4(vert, 0.0, 1.0);
    frag_uv = uv;
}
