from manim import *
config.pixel_height = 1920
config.pixel_width = 1080

class MatrixMinor(MovingCameraScene):
    def construct(self):
        self.camera.frame_width = 9
        self.camera.frame_height = 16



        intro_t = Tex("Laplace Expansion of a Determinant")
        intro_t.set_color_by_gradient(TEAL, YELLOW)
        intro_t.scale(0.5)
        self.play(Write(intro_t))
        self.play(intro_t.animate.scale(2))
        self.play(Unwrite(intro_t))

        n, k = 5, 5
        matrix_entries = [[f"a_{{{i+1}{j+1}}}" for j in range(k)] for i in range(n)]
        m = Matrix(matrix_entries)
        m.move_to(ORIGIN)
        self.play(Create(m), run_time = 1)

        # Zvýrazníme první řádek
        row1 = VGroup(*m.get_entries()[:k])
        self.play(row1.animate.set_color(YELLOW))
        title = Text(
            "Determinant expansion along the first row",
            font_size=32
        ).to_edge(UP)
        self.play(Write(title))
        self.wait(0.1)
        self.play(Unwrite(title))

        # Rovnice determinantu – první člen
        det_text = MathTex(r"\det(A) = a_{11} \cdot M_{11}", font_size=32)
        det_text.to_edge(DOWN)
        self.play(Write(det_text))
        self.wait(0.1)

        # === Funkce pro zobrazení minoru ===
        def show_minor(i, j, eq_text, show_definition=False):
            nonlocal det_text
            index = i * k + j
            a_ij = m.get_entries()[index]

            # Zvýrazni prvek
            highlight = SurroundingRectangle(a_ij, color=RED)
            self.play(Create(highlight))

            # Zvýrazni řádek a sloupec
            row_highlight = SurroundingRectangle(VGroup(*m.get_entries()[i*k:(i+1)*k]), color=BLUE)
            col_highlight = SurroundingRectangle(VGroup(*m.get_entries()[j::k]), color=GREEN)
            self.play(Create(row_highlight), Create(col_highlight))
            self.wait(0.1)

            # Minor se vykresí jen pokud show_definition=True
            if show_definition:
                minor_entries = []
                for r in range(n):
                    if r == i:
                        continue
                    row = []
                    for c in range(k):
                        if c == j:
                            continue
                        row.append(f"a_{{{r+1}{c+1}}}")
                    minor_entries.append(row)

                minor_matrix = Matrix(minor_entries)
                # Oddálíme kameru a posuneme nahoru
                self.play(
                    self.camera.frame.animate.scale(1.15).move_to(m.get_top() + UP)
                )
                minor_matrix.next_to(m, UP, buff=1.5)
                minor_def = MathTex(
                    f"M_{{{i+1}{j+1}}} = \\det(\\text{{Matrix without first column and row}})",
                    font_size=32
                ).next_to(minor_matrix, DOWN, buff=0.3)

                # Zobraz minor + definici
                self.play(Write(minor_matrix), Write(minor_def))
                self.wait(0.8)

                # Fade out minor a definici, kamera zpět
                self.play(FadeOut(minor_def), FadeOut(minor_matrix))
                self.play(
                    self.camera.frame.animate.scale(1/1.15).move_to(m.get_center())
                )

            # Aktualizuj vzorec
            new_eq = MathTex(eq_text, font_size=32).to_edge(DOWN)
            self.play(ReplacementTransform(det_text, new_eq))
            det_text = new_eq

            # FadeOut zvýraznění
            self.play(FadeOut(row_highlight), FadeOut(col_highlight), FadeOut(highlight))
            self.wait(0.3)

        # === Postupné zobrazení tří členů rozvoje ===
        show_minor(0, 0,
            eq_text=r"\det(A) = a_{11} \cdot M_{11}",
            show_definition=True
        )
        show_minor(0, 1, r"\det(A) = a_{11} \cdot M_{11} - a_{12} \cdot M_{12}")
        show_minor(0, 2, 
            eq_text=r"""
            \begin{aligned}
            \det(A) &= (-1)^{1+1}a_{11}M_{11} + (-1)^{1+2}a_{12}M_{12}+ (-1)^{1+3}a_{13}M_{13}
            \end{aligned}
            """
        )

        final_eq = MathTex(
            r"\det(A) = \sum_{j=1}^{5} (-1)^{1+j} a_{1j} M_{1j}",
            font_size=32
        ).to_edge(DOWN).shift(DOWN*0.5)
        self.play(ReplacementTransform(det_text, final_eq))
        det_text = final_eq

        final_box = SurroundingRectangle(det_text, color=YELLOW, buff=0.2)
        self.play(Create(final_box))
        self.wait(1)



        # OUTRO
        self.camera.frame.scale(1) 

        # DOPLNIT "..." ZA VSECHNY KONECNE OBJEKTY
        fin_group = VGroup(final_eq, final_box, m)
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