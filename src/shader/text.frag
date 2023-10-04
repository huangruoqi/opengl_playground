#version 330
uniform sampler2D tex;
in vec2 frag_uv;
out vec4 color;
void main() {
    color = texture(tex, frag_uv);
}
