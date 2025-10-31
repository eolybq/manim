from manim import *

class Outro(Scene):
    def construct(self):
        # OUTRO
        self.camera.frame.scale(1) 

        # DOPLNIT "..." ZA VSECHNY KONECNE OBJEKTY
        fin_group = VGroup(...)
        r_logo = Tex("R", font_size=144)
        r_logo.set_fill(opacity=0)
        r_logo.set_stroke(width=6, color=[TEAL, BLUE]).set_sheen_direction([1, 0, 0])
        r_logo.move_to(ORIGIN)


        chan_name_r = Tex("R", font_size=50)
        chan_name_r.set_fill(opacity=0)
        chan_name_r.set_stroke(width=2)
        chan_name = Tex("eal", font_size=40)
        chan_name.next_to(chan_name_r, RIGHT, buff = 0)

        chan_name_n = Tex("N", font_size=50)
        chan_name_n.set_fill(opacity=0)
        chan_name_n.set_stroke(width=2)
        chan_name_n.next_to(chan_name, RIGHT, buff=0.2)
        chan_name2 = Tex("umbers", font_size=40)
        chan_name2.next_to(chan_name_n, RIGHT, buff = 0)

        chan_name_text = VGroup(chan_name_r, chan_name, chan_name_n, chan_name2)
        chan_name_text.next_to(r_logo, DOWN, buff = 0.2)
        chan_name_text.set_color_by_gradient(TEAL, BLUE)


        self.play(ReplacementTransform(fin_group, r_logo), run_time = 1.5)
        self.play(Write(chan_name_text))
        self.wait(1)