from manim import *

class Logo(Scene):
    def construct(self):
        # první písmeno jako obrys
        t = Tex("R", font_size=144, color=WHITE)
        t.set_fill(opacity=0)          # odstraní výplň
        t.set_stroke(width=6, color=WHITE)  # nastaví obrys

        self.add(t)
