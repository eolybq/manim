from manim import *

class LinearR(Scene):
    def construct(self):
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
        intro_t.scale(1.5)
        intro_t.to_edge(UP, buff=2)


        ax1 = Axes(
            x_range=[40, 190, 20],
            y_range=[145165, 424051, 40_000],
            x_length=6,
            y_length=5,
            axis_config={"include_numbers": False}
        ).set_color_by_gradient(BLUE, TEAL)

        ax1.scale(0.5)
        ax1.move_to(ORIGIN)
        

        points = []
        for row in data:
            x = row['size']
            y = row['price']
            point = ax1.coords_to_point(x, y)
            points.append(Dot(point=point, color=BLUE).scale(0.5))



        x0, y0 = 40, 145165
        x1, y1 = 190, 424051


        start1 = ax1.c2p(x0, y0)
        end1 = ax1.c2p(x1 - 30, y1)
        line = Line(start1, end1)
        line.set_color_by_gradient(TEAL, RED)
        line.z_index = 10


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


        line.put_start_and_end_on(start_ols, end_ols),


        thumb_group = VGroup(intro_t, ax1, *[dot for dot in points], line, error_bars2)
        thumb_group.move_to(ORIGIN)
        self.add(thumb_group)
