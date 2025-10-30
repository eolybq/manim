from manim import *

class DeadWeightLoss(MovingCameraScene):
    def construct(self):
        self.camera.frame_width = 18
        self.camera.frame_height = 32
        f_size = 35


        ax1 = Axes(
            x_range = [0, 4],
            y_range = [0, 4],
            x_length=8,
            y_length=8,
            axis_config={"include_numbers": True},
            tips = True
        )

        # Initial state
        initial_text = Text("Deadweight loss")
        self.play(Write(initial_text))


        length = 3
        d = lambda x: -x + length
        s = lambda x: x

        graph_d = ax1.plot(d, x_range=[0, length], color = BLUE)
        d_end_point = graph_d.points[-1]
        d_label = MathTex("D").next_to(d_end_point, UR)

        graph_s = ax1.plot(s, x_range=[0, length], color = BLUE)
        s_end_point = graph_s.points[-1]
        s_label = MathTex("S").next_to(s_end_point, UR)
        
        optimum_p = Dot(ax1.c2p(length / 2, length / 2))
        optimum_p2 = Dot(ax1.c2p(length / 2, length / 2))
        optimum_p.z_index = 10
        optimum_p2.z_index = 10
        p_label = MathTex("E", color = GRAY).next_to(optimum_p, UP)

        self.play(self.camera.frame.animate.scale(0.5).move_to(ax1.get_center()))
        self.play(Unwrite(initial_text))

        optimum_text = Text("At first, market is effective", t2c = {"effective": GRAY},  font_size=f_size).add_updater(
            lambda m: m.move_to(self.camera.frame.get_top() + DOWN*3)
        )
        optimum_text.move_to([0, self.camera.frame_height/2 - 1, 0])


        group = VGroup(ax1, graph_s, graph_d, optimum_p, optimum_p2, s_label, d_label, p_label)
        self.play(Create(ax1), Create(graph_s), Create(graph_d), Create(s_label), Create(d_label))
        self.play(Write(optimum_text), Create(optimum_p), Write(p_label))
        self.add(optimum_p2)

        self.wait(1)


        # ZMV
        # body pro oblast mezi křivkami a osou y
        x_vals = np.linspace(1, length / 2, 50)
        points = [ax1.c2p(x, d(x)) for x in x_vals]              # horní křivka
        points += [ax1.c2p(x, s(x)) for x in x_vals[::-1]]       # dolní křivka zpět
        zmv = Polygon(*points, color=RED, fill_opacity=0.5)
        group.add(zmv)
        zmv.z_index = 9

        # Vynos dane
        x0, y0 = 0, 1       # levý dolní roh
        x1, y1 = 1, 2     # pravý horní roh
        width = ax1.c2p(x1,0)[0] - ax1.c2p(x0,0)[0]
        height = ax1.c2p(0,y1)[1] - ax1.c2p(0,y0)[1]
        center = ax1.c2p((x0+x1)/2,(y0+y1)/2)
        tax = Rectangle(width=width, height=height, color=DARK_BLUE, fill_opacity=0.5)
        tax.move_to(center)
        group.add(tax)

        # Přesun do noveho
        self.play(Unwrite(p_label), Unwrite(optimum_text))
        # group.remove(p_label)

        tax_text1 = Text("33% price tax imposed by government", t2c = {"33% price tax": DARK_BLUE},  font_size=f_size).add_updater(
            lambda m: m.move_to(self.camera.frame.get_top() + DOWN*3)
        )
        # animace přesunu bodů
        self.play(
            optimum_p.animate.move_to(ax1.c2p(1, 2)),
            optimum_p2.animate.move_to(ax1.c2p(1, 1)),
            # přidání polygonu a animace
            GrowFromEdge(tax, edge=RIGHT),
            Create(zmv),
            Write(tax_text1)
        )

        self.wait(1)
        self.play(Unwrite(tax_text1))

        zmv_text1 = Text("Tax creates Deadweight loss,\nwhere total utility is lost", t2c = {"Deadweight loss": RED}, font_size=f_size).add_updater(
            lambda m: m.move_to(self.camera.frame.get_top() + DOWN*3)
        )
        self.play(Write(zmv_text1))
        self.wait(1)
        self.play(Unwrite(zmv_text1))


        ax2 = Axes(
            x_range=[0, 1, 0.1],
            y_range=[0, 1, 0.1],
            x_length=8,
            y_length=8,
            x_axis_config={"include_numbers": True},
            tips = True
        )
        x_label = MathTex("Tax\\ rate").next_to(ax2.x_axis, DOWN)

        y_label = MathTex("Tax\\ income").move_to(ax2.y_axis.get_center() + LEFT * 0.4)
        y_label.rotate(PI/2)

        a, b, k = 1.2, 1.2, 5
        l = lambda x: k * (x**a) * ((1 - x)**b)

        graph_l = ax2.plot(l, color = YELLOW)


        tax_r = 0.33
        x_val = ValueTracker(tax_r)  # startovní pozice x
        vert_line = always_redraw(lambda: Line(
            start=ax2.c2p(x_val.get_value(), 0),
            end=ax2.c2p(x_val.get_value(), l(x_val.get_value())),
            color=DARK_BLUE
        ))
        # pohyblivá horizontální čára
        y_val = ValueTracker(l(tax_r))  # startovní hodnota y
        horiz_line = always_redraw(lambda: Line(
            start=ax2.c2p(0, y_val.get_value()),
            end=ax2.c2p(x_val.get_value(), y_val.get_value()),  # rozsah čáry na ose x
            color=DARK_BLUE
        ))

        group2 = VGroup(ax2, x_label, y_label, graph_l, vert_line, horiz_line)
        group2.shift(DOWN * 12)

        # group.animate.shift(UP),
        self.play(group.animate.shift(DOWN * 2), self.camera.frame.animate.scale(1.5).move_to((group.get_center() + group2.get_center())/2))

        f_size = 40

        l_text1 = Text("Laffer curve represents how\ntax income rises with tax rate", t2c = {"Laffer curve": YELLOW}, font_size=f_size).add_updater(
            lambda m: m.move_to(self.camera.frame.get_top() + DOWN*3)
        )

        self.play(Write(l_text1), Create(ax2.x_axis), Create(ax2.y_axis), Create(x_label), Create(y_label), Create(graph_l))
        self.play(Create(vert_line), Create(horiz_line))


        self.wait(1)
        self.play(Unwrite(l_text1))


        # ZMV2
        x_vals = np.linspace(0.75, length / 2, 50)
        points = [ax1.c2p(x, d(x)) for x in x_vals]              # horní křivka
        points += [ax1.c2p(x, s(x)) for x in x_vals[::-1]]       # dolní křivka zpět
        zmv2 = Polygon(*points, color=RED, fill_opacity=0.5)
        zmv2.z_index = 9


        # Vynos dane2
        x0, y0 = 0, 0.75      # levý dolní roh
        x1, y1 = 0.75, 2.25     # pravý horní roh
        width = ax1.c2p(x1,0)[0] - ax1.c2p(x0,0)[0]
        height = ax1.c2p(0,y1)[1] - ax1.c2p(0,y0)[1]
        center = ax1.c2p((x0+x1)/2,(y0+y1)/2)
        tax2 = Rectangle(width=width, height=height, color=DARK_BLUE, fill_opacity=0.5)
        tax2.move_to(center)


        l_text2 = Text("This is the maximum tax income,\nbut DWL rises aswell", t2c = {"DWL": RED}, font_size=f_size).add_updater(
            lambda m: m.move_to(self.camera.frame.get_top() + DOWN*3)
        )
        # animace přesunu bodů
        # animace posunu k ose y
        # animace pohybu čáry
        self.play(
            optimum_p.animate.move_to(ax1.c2p(0.75, 2.25)),
            optimum_p2.animate.move_to(ax1.c2p(0.75, 0.75)),
            Transform(zmv, zmv2),
            Transform(tax, tax2),
            x_val.animate.set_value(0.5),
            y_val.animate.set_value(l(0.5)),
            Write(l_text2),
            run_time = 1.5
        )




        self.wait(1)
        self.play(Unwrite(l_text2))


        # ZMV3
        x_vals = np.linspace(0.5, length / 2, 50)
        points = [ax1.c2p(x, d(x)) for x in x_vals]              # horní křivka
        points += [ax1.c2p(x, s(x)) for x in x_vals[::-1]]       # dolní křivka zpět
        zmv3 = Polygon(*points, color=RED, fill_opacity=0.5)
        zmv3.z_index = 9


        # Vynos dane3
        x0, y0 = 0, 0.5      # levý dolní roh
        x1, y1 = 0.5, 2.5     # pravý horní roh
        width = ax1.c2p(x1,0)[0] - ax1.c2p(x0,0)[0]
        height = ax1.c2p(0,y1)[1] - ax1.c2p(0,y0)[1]
        center = ax1.c2p((x0+x1)/2,(y0+y1)/2)
        tax3 = Rectangle(width=width, height=height, color=DARK_BLUE, fill_opacity=0.5)
        tax3.move_to(center)

        l_text3 = Text("Past Laffer curve maximum,\nonly DWL rises", t2c={"Laffer curve": YELLOW, "DWL": RED}, font_size=f_size).add_updater(
            lambda m: m.move_to(self.camera.frame.get_top() + DOWN*3)
        )

        # animace přesunu bodů
        # animace posunu k ose y
        # animace pohybu čáry
        self.play(
            optimum_p.animate.move_to(ax1.c2p(0.5, 2.5)),
            optimum_p2.animate.move_to(ax1.c2p(0.5, 0.5)),
            Transform(zmv, zmv3),
            Transform(tax, tax3),
            x_val.animate.set_value(0.66),
            y_val.animate.set_value(l(0.66)),
            Write(l_text3),
            run_time = 1.5
        )

        self.wait(1)



        # animace přesunu bodů
        # animace posunu k ose y
        # animace pohybu čáry
        self.play(
            optimum_p.animate.move_to(ax1.c2p(1.5, 1.5)),
            optimum_p2.animate.move_to(ax1.c2p(1.5, 1.5)),
            Uncreate(zmv),
            Uncreate(tax),
            x_val.animate.set_value(0),
            y_val.animate.set_value(l(0)),
            Unwrite(l_text3),
            run_time = 1.5
        )

        p_label = MathTex("E", color = GRAY).next_to(optimum_p, UP)
        zmv_text2 = Text("Because of DWL,\n market isn't in equilibrium", t2c = {"DWL": RED}, font_size=f_size).add_updater(
            lambda m: m.move_to(self.camera.frame.get_top() + DOWN*3)
        )

        self.play(Unwrite(group2), self.camera.frame.animate.scale(0.75).move_to(ax1.get_center()), Write(p_label), Write(zmv_text2))

        self.play(Unwrite(group), Unwrite(p_label), Unwrite(zmv_text2))

        end_text = Text("Government get tax income,\n part of total utility is lost", t2c = {"tax income": DARK_BLUE, "lost": RED})
        self.play(Write(end_text))

        self.wait(1)