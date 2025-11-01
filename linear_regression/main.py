from manim import *

class LinearR(Scene):
    def construct(self):
        # ---SHORTS POTREBUJI THUMBNAIL PRIMO VE VIDEU---
        # img = ImageMobject("media/images/thumbnail/thumbnail.png")
        # img.scale(0.6)
        # self.add(img)
        # self.wait(0.01)
        # self.remove(img)


        f_size = 20
        config.frame_width = 9

        data = np.array([
            (189968, 50),
            (220037, 55),
            (155165, 60),
            (212933, 65),
            (182058, 70),
            (281195, 75),
            (212047, 80),
            (250027, 85),
            (180181, 90),
            (286343, 95),
            (245150, 100),
            (230071, 105),
            (311202, 110),
            (243050, 115),
            (287026, 120),
            (261191, 125),
            (328020, 130),
            (278151, 135),
            (339980, 140),
            (290174, 145),
            (354034, 150),
            (314008, 155),
            (362005, 160),
            (339001, 165),
            (400031, 170),
            (363111, 175),
            (414051, 180)
        ], dtype=[('price', 'i4'), ('size', 'i4')]) 


        intro_t = Tex("OLS Linear Regression")
        intro_t.set_color_by_gradient(TEAL, RED)
        intro_t.scale(0.5)

        self.play(Write(intro_t))
        self.play(intro_t.animate.scale(1.5))
        self.play(Unwrite(intro_t))


        first_t = Text("Imagine you have 2 variables:\nprice and size of a house")
        first_t.font_size = f_size
        first_t.set_color_by_gradient(RED, BLUE)
        first_t.to_edge(UP, buff = 0.8)

        
        table_data = [["Price ($)", "Size (m²)"]]
        for row in data[5:15]:
            table_data.append([f"{row['price']:,}", str(row['size'])])

        table = Table(
            table_data,
            # col_widths=[3, 2],
            row_labels=None,
            include_outer_lines=False
        )
        table.scale(0.3)
        table.set_color_by_gradient(RED, BLUE)


        self.play(
            AnimationGroup(
                Write(first_t),
                Create(table),
                lag_ratio=0.6
            )
        )
        self.wait(0.5)
        self.play(
            AnimationGroup(
                Unwrite(first_t),
                Uncreate(table),
            )
        )


        sec_t = Text("We can see that price rises as size rises")
        sec_t.font_size = f_size
        sec_t.set_color_by_gradient(TEAL, BLUE)
        sec_t.to_edge(UP, buff = 0.8)

        ax1 = Axes(
            x_range=[40, 190, 20],
            y_range=[145165, 424051, 40_000],
            x_length=6,
            y_length=5,
            axis_config={"include_numbers": True}
        ).set_color_by_gradient(BLUE, TEAL)
        x_label = Text("Size (m²)").next_to(ax1.x_axis.get_center(), DOWN, buff=0.4).scale(0.7).set_color(BLUE)
        y_label = Text("Price ($)").next_to(ax1.y_axis.get_center(), LEFT, buff=0.2).scale(0.7).set_color(BLUE)
        y_label.rotate(PI/2)

        plot1 = VGroup(ax1, x_label, y_label)
        plot1.scale(0.5)
        plot1.move_to(ORIGIN)
        

        points = []
        for row in data:
            x = row['size']
            y = row['price']
            point = ax1.coords_to_point(x, y)
            points.append(Dot(point=point, color=BLUE).scale(0.5))


        self.play(
            AnimationGroup(
                Create(ax1),
            )
        )
        self.play(
             AnimationGroup(
                Write(sec_t),
                Write(x_label),
                Write(y_label),
                *[Write(dot) for dot in points]
             )
        )
        # self.wait(2)


        third_t = Text("We can try to approximate\nthis relationship\nwith lines of different slopes", t2c={"lines": RED})
        third_t.font_size = f_size
        third_t.set_color_by_gradient(TEAL, RED)
        third_t.to_edge(UP, buff = 0.8)
        
        self.play(Unwrite(sec_t))



        x0, y0 = 40, 145165
        x1, y1 = 190, 424051


        start1 = ax1.c2p(x0, y0)
        end1 = ax1.c2p(x1 - 30, y1)
        line = Line(start1, end1)
        line.set_color_by_gradient(TEAL, RED)
        line.z_index = 10
        self.play(
            Write(third_t),
            Create(line)
        )
        self.wait(0.5)


        start2 = ax1.c2p(x0, y0)
        end2 = ax1.c2p(x1 - 60, y1)
        self.play(
            line.animate.put_start_and_end_on(
                start2,
                end2
            )
        )


        start3 = ax1.c2p(x0, y0)
        end3 = ax1.c2p(x1, y1 - 100_000)
        
        self.play(
            line.animate.put_start_and_end_on(
                start3,
                end3
            )
        )


        fourth_t = Text("Or different shifts along y axis")
        fourth_t.font_size = f_size
        fourth_t.set_color_by_gradient(RED, TEAL)
        fourth_t.to_edge(UP, buff = 0.8)

        start4 = ax1.c2p(x0, y0 + 60_000)
        end4 = ax1.c2p(x1, y1 - 100_000 + 60_000)

        self.play(Unwrite(third_t))
        self.play(
            AnimationGroup(
                Write(fourth_t),
                line.animate.put_start_and_end_on(
                    start4,
                    end4
                )
            )
        )


        start5 = ax1.c2p(x0, y0 + 30_000)
        end5 = ax1.c2p(x1, y1 - 100_000 + 30_000)

        self.play(
            line.animate.put_start_and_end_on(
                start5,
                end5
            )
        )


        fifth_t = Text("The distance from each data point\nrepresents line's error")
        fifth_t.font_size = f_size
        fifth_t.set_color_by_gradient(TEAL, YELLOW)
        fifth_t.to_edge(UP, buff = 0.8)


        def create_error_bars_from_line(line_obj):
            rects = VGroup()
            start = ax1.p2c(line_obj.get_start())
            end = ax1.p2c(line_obj.get_end())

            x0_line, y0_line = start
            x1_line, y1_line = end

            for dot in points:
                x_data = ax1.p2c(dot.get_center())[0]
                # Odpovídající y na čáře (v datových souřadnicích)
                y_line = y0_line + (y1_line - y0_line)/(x1_line - x0_line) * (x_data - x0_line)
                line_y = ax1.c2p(x_data, y_line)[1]
                dot_x, dot_y = dot.get_center()[0], dot.get_center()[1]

                rect = Rectangle(
                    width=0.000005,  # šířka obdélníku
                    height=abs(dot_y - line_y),
                    color=YELLOW
                )
                rect.set_fill(YELLOW, opacity=0.2)
                rect.set_stroke(YELLOW, width=1, opacity=0.6)
                rect.move_to([(dot_x + dot_x)/2, (dot_y + line_y)/2, 0])
                rects.add(rect)
            return rects

        error_bars = create_error_bars_from_line(line)
        # error_bars = create_error_bars_from_line(line)
        # error_bars.add_updater(lambda r: r.become(create_error_bars_from_line(line)))



        self.play(Unwrite(fourth_t))
        self.play(
            AnimationGroup(
                Write(fifth_t),
                Create(error_bars)
            )
        )
        self.wait(0.5)


        sixth_t = Text("We take each distance\nin square to eliminate signs")
        sixth_t.font_size = f_size
        sixth_t.set_color_by_gradient(TEAL, YELLOW)
        sixth_t.to_edge(UP, buff = 0.8)


        self.play(Unwrite(fifth_t)) 
        self.play(
            AnimationGroup(
                Write(sixth_t),
                AnimationGroup(
                    *[r.animate.stretch_to_fit_width(r.get_height()) for r in error_bars],
                    lag_ratio=0.08
                )
            )
        )


        seventh_t = Text("The line which creates\nthe least sum of those squares (OLS)\nis our regression line", color=TEAL, t2c={"those squares": YELLOW, "regression line": RED})
        seventh_t.font_size = f_size
        seventh_t.to_edge(UP, buff = 0.8)

        x = data['size'].astype(float)
        y = data['price'].astype(float)
        # OLS vzorec pro lineární regresi: m = slope, b = intercept
        x_mean = np.mean(x)
        y_mean = np.mean(y)
        m = np.sum((x - x_mean)*(y - y_mean)) / np.sum((x - x_mean)**2)
        b = y_mean - m * x_mean

        x0, x1 = ax1.x_range[0], ax1.x_range[1]  # např. 40, 190

        y0 = m * x0 + b
        y1 = m * x1 + b

        start_ols = ax1.c2p(x0, y0)
        end_ols = ax1.c2p(x1, y1)


        line_ols = Line(start_ols, end_ols).set_color_by_gradient(TEAL, RED)
        error_bars2 = create_error_bars_from_line(line_ols)
        for rect in error_bars2:
            rect.stretch_to_fit_width(rect.height)




        self.play(Unwrite(sixth_t))
        self.play(
            AnimationGroup(
                Write(seventh_t),
                line.animate.put_start_and_end_on(start_ols, end_ols),
                Transform(error_bars, error_bars2)
            )
        )
        self.wait(2)


        # OUTRO
        # self.camera.frame.scale(1) 

        # DOPLNIT "..." ZA VSECHNY KONECNE OBJEKTY
        fin_group = VGroup(ax1, x_label, y_label, seventh_t, *[dot for dot in points], error_bars, line)
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