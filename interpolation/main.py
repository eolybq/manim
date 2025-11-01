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

        text_uvod = Text("Lagrange Interpolation", font_size=48)
        text_uvod.scale(0.5)
        text_im = Text("Imagine you are given n points from a function.\n How would you approximate the function?",t2c={" n ": GREEN}, font_size=28).to_edge(UP).shift(UP*3)
        text_le = Text("For this, we can use a tool called Lagrange\nInterpolation, constructing Lagrange Polynomial", font_size=28, t2c={"Lagrange\nInterpolation": BLUE, "Lagrange Polynomial": RED}).to_edge(UP).shift(UP*3)
        text_hu = Text("Let's see how it works").to_edge(UP).shift(UP*3)

        self.play(Write(text_uvod))
        self.play(text_uvod.animate.scale(1.5))
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
        self.wait(0.5)
        self.play(FadeOut(text_vy), FadeOut(text_math), FadeOut(rect), FadeOut(formula))
        
        #3. PART
        L0 = lambda x: ((x-1)*(x-2)*(x-3)*(x-4)) / ((0-1)*(0-2)*(0-3)*(0-4))
        L1 = lambda x: ((x-0)*(x-2)*(x-3)*(x-4)) / ((1-0)*(1-2)*(1-3)*(1-4))
        L2 = lambda x: ((x-0)*(x-1)*(x-3)*(x-4)) / ((2-0)*(2-1)*(2-3)*(2-4))
        L3 = lambda x: ((x-0)*(x-1)*(x-2)*(x-4)) / ((3-0)*(3-1)*(3-2)*(3-4))
        L4 = lambda x: ((x-0)*(x-1)*(x-2)*(x-3)) / ((4-0)*(4-1)*(4-2)*(4-3))

        P = lambda x: 2*L0(x) + 0*L1(x) + 2*L2(x) + 1*L3(x) + 4*L4(x)

        text_ex = Text("Let's see how this looks for our first point:", font_size=28).move_to(self.camera.frame.get_center() + UP*6.3)

        formula_L0_raw = MathTex(
        r"L_0(x) = (x-1)(x-2)(x-3)(x-4)",
        font_size=40
        ).next_to(text_ex, DOWN, buff=0.8)

        text_div = MathTex(
            r"""
            \begin{aligned}
            &\text{To make sure } L_0(0) = 1, \text{ we divide} \\
            &\text{by its value at } x_0:
            \end{aligned}
            """,
            font_size=40
        )

        # Pozice
        text_div.next_to(formula_L0_raw, DOWN, buff=1)

        formula_L0 = MathTex(
        r"L_0(x) = \frac{(x-1)(x-2)(x-3)(x-4)}{(0-1)(0-2)(0-3)(0-4)}",
        font_size=40
        ).next_to(text_div, DOWN, buff=0.8)



        ax3 = Axes(
            
            x_range=[0, 5, 1],
            y_range=[0, 5, 1],
            x_length=8,
            y_length=6,
            axis_config={"include_numbers": True},
        )
        ax3.move_to(self.camera.frame.get_center(), UP * 0.65)

        self.play(Write(text_ex))
        self.play(Create(ax3), run_time=2)
        dot31, dot32, dot33, dot34, dot35 = Dot(ax3.c2p(0,2), color=RED), Dot(ax3.c2p(1,0), color=YELLOW), Dot(ax3.c2p(2,2), color=PINK), Dot(ax3.c2p(3,1), color=GREEN), Dot(ax3.c2p(4,4), color=BLUE)
        self.play(Create(dot31),Create(dot32),Create(dot33), Create(dot34), Create(dot35))
        self.wait(1)

        self.play(FadeOut(text_ex), Write(formula_L0_raw))

        L0_RAW = ax3.plot(lambda x: (x-1)*(x-2)*(x-3)*(x-4), x_range=[0.65,4.3])
        self.play(Create(L0_RAW))
        line_v1 = DashedLine(start=ax3.c2p(0, 0), end=ax3.c2p(0, 2), color=RED, dash_length=0.1)
        line_v2 = DashedLine(ax3.c2p(1, 0), ax3.c2p(1, 0), color=YELLOW, dash_length=0.1)
        line_v3 = DashedLine(ax3.c2p(2, 0), ax3.c2p(2, 2), color=PINK, dash_length=0.1)
        line_v4 = DashedLine(ax3.c2p(3, 0), ax3.c2p(3, 1), color=GREEN, dash_length=0.1)
        line_v5 = DashedLine(ax3.c2p(4, 0), ax3.c2p(4, 4), color=BLUE, dash_length=0.1)

        self.play(Create(line_v1), Create(line_v2), Create(line_v3),Create(line_v4), Create(line_v5))
        self.wait(1)

        self.play(Write(text_div))
        self.play(Write(formula_L0))
        self.wait(0.5)
        self.play(FadeOut(formula_L0_raw), FadeOut(text_div))

        self.play(formula_L0.animate.move_to(self.camera.frame.get_center() + UP*6), run_time=1)
        
        L0_l = ax3.plot(L0, x_range=[0, 4.3], color=RED)
        self.play(Create(L0_l), FadeOut(L0_RAW))

        self.wait(1)

        # Vzorec pro L1
        formula_L1 = MathTex(
            r"L_1(x) = \frac{(x-0)(x-2)(x-3)(x-4)}{(1-0)(1-2)(1-3)(1-4)}",
            font_size=40
        ).next_to(formula_L0, DOWN, buff=1.2)
        self.play(Write(formula_L1))
        self.wait(0.5)

        # Tři vertikální tečky
        dots = MathTex(r"\vdots", font_size=36).next_to(formula_L1, DOWN, buff=0.5)
        self.play(Write(dots))
        self.wait(0.5)

        # Text o součtu
        sum_text = Text("Now we sum them up to get the polynomial:", font_size=28).next_to(dots, DOWN, buff=0.8)
        self.play(Write(sum_text))

        # Obecný vzorec pro Lagrangeův polynom
        general_formula = MathTex(
            r"P(x) = \sum_{i=0}^{n} y_i L_i(x), \quad L_i(x) = \prod_{\substack{j=0 \\ j \neq i}}^{n} \frac{x-x_j}{x_i-x_j}",
            font_size=40
        ).next_to(sum_text, DOWN, buff=0.8)
        self.play(Write(general_formula))
        self.wait(1)

        L1_l = ax3.plot(L1, x_range=[0, 4.3], color=YELLOW)
        L2_l = ax3.plot(L2, x_range=[0, 4.3], color=PINK)
        L3_l = ax3.plot(L3, x_range=[0, 4.3], color=GREEN)
        L4_l = ax3.plot(L4, x_range=[0, 4.3], color=BLUE)

        lGroup = VGroup(L0_l, L1_l, L2_l, L3_l, L4_l)

        self.play(Create(L1_l),Create(L2_l),Create(L3_l),Create(L4_l))
        self.wait(1)

        P_final = ax3.plot(P, x_range=[0,4.3])
        self.play(Transform(lGroup, P_final))
        self.wait(1)

        #TODO OUTRO