from manim import *

class thumbnail(Scene):
    def construct(self):
        config.frame_width = 9
        text_uvod = Text("Lagrange Interpolation").scale(0.5)
        text_uvod.set_color_by_gradient(TEAL, PURPLE)
        ax3 = Axes(
            
            x_range=[0, 5, 1],
            y_range=[0, 5, 1],
            x_length=8,
            y_length=6,
            axis_config={"include_numbers": True},
        ).set_color_by_gradient(BLUE,TEAL).scale(0.5).next_to(text_uvod, DOWN, buff=0.7)
        
        L0 = lambda x: ((x-1)*(x-2)*(x-3)*(x-4)) / ((0-1)*(0-2)*(0-3)*(0-4))
        L1 = lambda x: ((x-0)*(x-2)*(x-3)*(x-4)) / ((1-0)*(1-2)*(1-3)*(1-4))
        L2 = lambda x: ((x-0)*(x-1)*(x-3)*(x-4)) / ((2-0)*(2-1)*(2-3)*(2-4))
        L3 = lambda x: ((x-0)*(x-1)*(x-2)*(x-4)) / ((3-0)*(3-1)*(3-2)*(3-4))
        L4 = lambda x: ((x-0)*(x-1)*(x-2)*(x-3)) / ((4-0)*(4-1)*(4-2)*(4-3))

        L0_l = ax3.plot(L0, x_range=[0, 4.3], color=RED)
        L1_l = ax3.plot(L1, x_range=[0, 4.3], color=YELLOW)
        L2_l = ax3.plot(L2, x_range=[0, 4.3], color=PINK)
        L3_l = ax3.plot(L3, x_range=[0, 4.3], color=GREEN)
        L4_l = ax3.plot(L4, x_range=[0, 4.3], color=BLUE)

        t_group = VGroup(
            ax3, text_uvod, L0_l,L1_l,L2_l,L3_l,L4_l
        ).move_to(ORIGIN)
        self.add(ax3, L0_l,L1_l,L2_l,L3_l,L4_l, text_uvod)