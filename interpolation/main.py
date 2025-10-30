from manim import *

class Lagrange(MovingCameraScene):
    def construct(self):
        self.camera.frame_width = 9
        self.camera.frame_height = 16
        ax1 = Axes(
            
            x_range=[0, 5, 1],
            y_range=[0, 5, 1],
            x_length=8,
            y_length=6,
            axis_config={"include_numbers": True},
        )
        # title = Text(
        #     "Science Prodigy",
        #     font="Audiowide",
        #     color=BLUE_B,
        #     weight=BOLD
        # ).scale(1.5)

        # self.play(FadeIn(title, shift=UP, scale=0.8), run_time=2)
        # self.play(
        #     title.animate.scale(0.8).to_corner(UL),
        #     run_time=2
        # )
        # self.wait(0.2)

        text_uvod = Text("Lagrange Interpolation", font_size=48)
        text_im = Text("Imagine you are given n points from a function.\n How would you approximate the function?",t2c={" n ": GREEN}, font_size=28).to_edge(UP).shift(UP*3)
        text_le = Text("For this, we can use a tool called Lagrange\nInterpolation, constructing Lagrange Polynomial", font_size=28, t2c={"Lagrange\nInterpolation": BLUE, "Lagrange Polynomial": RED}).to_edge(UP).shift(UP*3)
        text_hu = Text("Let's see how it works").to_edge(UP).shift(UP*3)

        self.play(Write(text_uvod))
        # self.play(FadeOut(title))
        self.play(Unwrite(text_uvod))

        self.play(Create(ax1), run_time=2)
        dot1, dot2, dot3, dot4, dot5 = Dot(ax1.c2p(0,2), color=RED), Dot(ax1.c2p(1,0), color=YELLOW), Dot(ax1.c2p(2,2), color=PINK), Dot(ax1.c2p(3,1), color=GREEN), Dot(ax1.c2p(4,4), color=BLUE)
        self.play(Create(dot1),Create(dot2),Create(dot3), Create(dot4), Create(dot5))
        self.wait(1)

        self.play(Write(text_im))
        self.wait(0.2)
        self.play(FadeOut(text_im))
        self.wait(1)

        self.play(Write(text_le))
        self.wait(1)
        polynom_showcase = ax1.plot(lambda x: 0.5833*x**4 - 4.6663*x**3 + 11.9154*x**2 - 9.8316*x + 1.9992, x_range=[0,4], color=RED)
        self.play(Create(polynom_showcase))
        self.play(FadeOut(text_le))
        self.play(Write(text_hu))

        # 2. PART
        self.play(self.camera.frame.animate.scale(1.5))
        self.play(self.camera.frame.animate.shift(RIGHT*10))
        self.play(self.camera.frame.animate.scale(2/3))

        text_fp = Text("We will need a specific polynomial for every point.", font_size=28).move_to(self.camera.frame.get_center() + UP*6.3)
        text_tp = Text("This polynomial returns the value 1 at its\n corresponding point and 0 at all other points:",t2c={"1": RED, "0": BLUE}, font_size=28).next_to(text_fp, DOWN, buff=2)
        formula = MathTex(r"L_i(x_j) = \begin{cases} 1, & \text{if } j = i \\ 0, & \text{if } j \neq i \end{cases}",font_size=50).next_to(text_tp, DOWN, buff=1.2)
        text_vy = Text("That means:",
            font_size=28).next_to(formula, DOWN, buff=0.8)
        text_math = MathTex(r"(x-x_0)\dots(x-x_{i-1})(x-x_{i+1})\dots(x-x_n) = 0",font_size=40).next_to(text_vy, DOWN, buff=0.8)
        text_j = Text(
            "If we plug in $x = x_j$ (where $j \\neq i$),\n one term of the product becomes 0, "
            "so the entire polynomial is 0.",
            font_size=28
        ).next_to(text_math, DOWN, buff=0.8)


        L0 = lambda x: ((x-1)*(x-2)*(x-3)*(x-4)) / ((0-1)*(0-2)*(0-3)*(0-4))
        L1 = lambda x: ((x-0)*(x-2)*(x-3)*(x-4)) / ((1-0)*(1-2)*(1-3)*(1-4))
        L2 = lambda x: ((x-0)*(x-1)*(x-3)*(x-4)) / ((2-0)*(2-1)*(2-3)*(2-4))
        L3 = lambda x: ((x-0)*(x-1)*(x-2)*(x-4)) / ((3-0)*(3-1)*(3-2)*(3-4))
        L4 = lambda x: ((x-0)*(x-1)*(x-2)*(x-3)) / ((4-0)*(4-1)*(4-2)*(4-3))

        P = lambda x: 2*L0(x) + 0*L1(x) + 2*L2(x) + 1*L3(x) + 4*L4(x)


        ax2 = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 5, 1],
            x_length=8,
            y_length=6,
            axis_config={"include_numbers": True}
        )
        ax2.move_to(self.camera.frame.get_center())
        dot21, dot22, dot23, dot24, dot25 = Dot(ax2.c2p(0,2), color=RED), Dot(ax2.c2p(1,0), color=YELLOW), Dot(ax2.c2p(2,2), color=PINK), Dot(ax2.c2p(3,1), color=GREEN), Dot(ax2.c2p(4,4), color=BLUE)
        self.play(Write(text_fp))
        self.wait()

        self.play(FadeOut(text_fp), Write(text_tp))
        self.play(Write(formula))

        rect = SurroundingRectangle(formula, color=YELLOW, buff=0.2)
        self.play(Create(rect))
        self.wait(1)
        self.play(Write(text_vy), Write(text_math), FadeOut(text_tp))
        self.play(Write(text_j))