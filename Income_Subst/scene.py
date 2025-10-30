from manim import *
from sympy import symbols, Eq, solve
import math

config.pixel_height = 1920
config.pixel_width = 1080


class Mikro(MovingCameraScene):
    def construct(self):
        self.camera.frame_width = 9
        self.camera.frame_height = 16
        ax = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 5, 1],
            x_length=6,
            y_length=6,
            axis_config={"include_numbers": True},
        )
        self.add(ax)
        x_label = ax.get_x_axis_label("x")
        y_label = ax.get_y_axis_label("y")
        x_label.next_to(ax.x_axis.get_end(), DOWN)
        y_label.next_to(ax.y_axis.get_end(), LEFT).shift(DOWN * 0.2)
        self.add(x_label, y_label)
        #ZAKLADNI PARAMETRY
        I = 2
        px = 1   
        py = 1   
        k = 1

        #ROZPOCTOVA LINIE S ROZPOCTEM I
        budget_line = ax.plot(lambda x: (I - px*x)/py, x_range=[0, I/px], color=BLUE)

        budget_line2 = ax.plot(lambda x: (I - px*x)/py, x_range=[0, I/px], color=BLUE)

        #INDIFERENCNI KRIVKA S VYPOCTEM PRUSECIKU (OPTIMA)
        x_sym = symbols('x')
        eq = Eq(k/x_sym, (I - px*x_sym)/py)
        sol = solve(eq, x_sym)
        x_opt = float(sol[0])
        y_opt = (I - px*x_opt)/py
        indifference_curve_initial = ax.plot(lambda x: k/x, x_range=[0.3, 4], color=RED)
        indifference_curve_old = ax.plot(lambda x: k/x, x_range=[0.3, 4], color=RED)
        optimum = Dot(ax.c2p(x_opt,y_opt))
        optimum.z_index = 10

        self.add(budget_line,budget_line2, indifference_curve_initial, indifference_curve_old)
        self.play(Create(optimum))
        
        # Text k původnímu optimu
        text1 = Text("Initial consumption optimum", font_size=24).to_edge(UP)
        self.play(Write(text1))
        self.wait(1)
        self.play(Unwrite(text1))

        #ZLEVNENI STATKU X A NOVY SKLON
        px2 = 0.5
        se_budget_line = ax.plot(lambda x: (I - px2*x)/py, x_range=[0,I/px2], color=GREEN)
        se_budget_line2 = ax.plot(lambda x: (I - px2*x)/py, x_range=[0,I/px2], color=GREEN)

        self.add(budget_line, budget_line2)
        self.wait(1)

        text2 = Text("Price of X decreases, budget line rotates", font_size=24, t2c={"budget line": GREEN}).to_edge(UP)
        self.play(Transform(budget_line, se_budget_line), Write(text2))
        self.wait(0.7)
        self.add(se_budget_line2)
        self.play(Unwrite(text2))
        self.wait(0.7)

        #POSUNUTI NA STEJNY PROSPECH A POMOCNA LINIE
        I_new = 2 * (k * px2) ** 0.5
        x_max = I_new / px2
        se_budget_line_paralel = ax.plot(lambda x: (I_new - px2*x)/py, x_range=[0,x_max], color=GREEN)

        text3 = Text("Income adjusted to reach previous utility level.", line_spacing=1.0,font_size=24).to_edge(UP)
        text3_o = Text("New optimum emerges", line_spacing=1.0,font_size=24, t2c = {"optimum": YELLOW}).next_to(text3, DOWN, buff=0.2)
        self.play(Transform(budget_line, se_budget_line_paralel), Write(text3))
        self.play(Write(text3_o))
        optimum2 = Dot(ax.c2p(math.sqrt(2), math.sqrt(2)/2), color=YELLOW)
        self.play(Create(optimum2))
        #SIPKA
        y_decrease = Arrow(start=ax.c2p(-0.5,1),end=ax.c2p(-0.5, math.sqrt(2)/2), stroke_width=10,max_stroke_width_to_length_ratio = 10, color=RED)
        x_increase = Arrow(start=ax.c2p(1,-0.5),end=ax.c2p(math.sqrt(2), -0.5), stroke_width=10,max_stroke_width_to_length_ratio = 10, color=RED)
        self.play(GrowArrow(y_decrease), GrowArrow(x_increase))
        self.wait(1)
        self.play(Unwrite(text3), Unwrite(text3_o))

        #DUCHODOVY EFEKT Z POMOCNE NA NOVOU, VYSSI INDIF KRIVKA
        
        
        x_new = symbols('x_new', positive=True)
        k_new = symbols('k_new', positive=True)

        # podminka tangency: y' = -k/x^2 = -px2/py
        eq_slope = Eq(k_new / x_new**2, px2 / py)

        # podminka pruseciku: y = k/x = rozpoctova linie
        eq_intercept = Eq(k_new / x_new, (I - px2 * x_new)/py)

        sol_new = solve([eq_slope, eq_intercept], (x_new, k_new))
        x_opt_new_val = float(sol_new[0][0])
        k_new_val = float(sol_new[0][1])
        y_opt_new_val = (I - px2 * x_opt_new_val)/py

        indifference_curve_new = ax.plot(lambda x: k_new_val / x, x_range=[0.5, 4], color=RED)
        optimum_new = Dot(ax.c2p(x_opt_new_val, y_opt_new_val), color=LIGHT_BROWN)

        y_increase = Arrow(start=ax.c2p(-0.75,math.sqrt(2)/2),end=ax.c2p(-0.75, y_opt_new_val), stroke_width=10,max_stroke_width_to_length_ratio = 10, color=WHITE)
        x_increase2 = Arrow(start=ax.c2p(math.sqrt(2) -0.15,-0.75),end=ax.c2p(x_opt_new_val + 0.15, -0.75), stroke_width=10,max_stroke_width_to_length_ratio = 10, color=WHITE)

        text4 = Text("Income effect takes in place, utility rises:\nshift from lower to higher indifference curve",line_spacing=1.0, t2c={"indifference curve": RED}, font_size=24).to_edge(UP)
        self.play(Transform(indifference_curve_initial, indifference_curve_new), Write(text4))
        self.play(Create(optimum_new), indifference_curve_old.animate.set_stroke(ORANGE, opacity=0.5))
        self.play(GrowArrow(y_increase), GrowArrow(x_increase2))

        self.wait(1)