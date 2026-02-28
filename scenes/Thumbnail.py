from manim import *
import math
import numpy as np

class Thumbnail(Scene):
    def construct(self):
        # =========================
        # Hintergrund / Ebene
        # =========================
        plane = NumberPlane(
            background_line_style={"stroke_opacity": 0.35}
        )
        plane.set_z_index(0)
        self.add(plane)

        # =========================
        # Titel
        # =========================
        title = Text(
            "Householder Transformation",
            font_size=72
        ).to_edge(UP, buff=0.4)

        title.add_background_rectangle(
            buff=0.25,
            opacity=0.85
        )
        title.set_z_index(9)
        self.add(title)

        # =========================
        # Householder-Formel GANZ OBEN
        # =========================
       

        

        # =========================
        # Einheitsnormale v
        # =========================
        a, b = 1 / math.sqrt(2), -1 / math.sqrt(2)
        v = Arrow(
            ORIGIN,
            [a, b, 0],
            color=YELLOW,
            buff=0
        )
        v_label = MathTex(r"\vec{v}").next_to(v.get_end(), RIGHT, buff=0.15)

        # =========================
        # Vektor x und x'
        # =========================
        x = Arrow(
            ORIGIN,
            [3, 0, 0],
            color=GREEN,
            buff=0
        )
        x_label = MathTex(r"\vec{x}").next_to(x.get_end(), UP, buff=0.15)

        xs = Arrow(
            ORIGIN,
            [0, 3, 0],
            color=GREEN,
            buff=0
        )
        xs_label = MathTex(r"\vec{x}'").next_to(
            xs.get_end(),
            LEFT + DOWN * 0.3,
            buff=0.15
        )

        dashed = DashedLine(
            x.get_end(),
            xs.get_end(),
            color=GREY
        )

        # =========================
        # Hyperplane (orthogonal zu v)
        # =========================
        dx, dy = -b, a
        L = 5.6
        hyperplane = Line(
            [-L * dx, -L * dy, 0],
            [ L * dx,  L * dy, 0],
            color=BLUE
        ).set_stroke(width=6)

        line_label = MathTex(r"\text{Hyperplane}")
        line_label.scale(0.8)
        line_label.next_to(hyperplane.get_end(), DOWN*6, buff=0.2)

        # =========================
        # Szene zusammenbauen
        # =========================
        geometry = VGroup(
            plane,
            hyperplane, line_label,
            v, v_label,
            x, x_label,
            xs, xs_label,
            dashed
        )

        geometry.shift(DOWN)
        self.add(geometry)

       # Obere Formel (kurz, mit Phantom für gleiche Größe – optional)
        # Householder-Formel (voll)
        householder1 = MathTex(
            r"H = I - \frac{2 v v^{\top}}{v^{\top} v}",
            font_size=72
        ).to_corner(UL, buff=0.8)

        # Box um die Formel
        H1Box = SurroundingRectangle(
            householder1,
            color=RED,
            buff=0.25
        )

        # Z-Order (über Plane & Geometrie)
        householder1.set_z_index(10)
        H1Box.set_z_index(9)

        # Optional: gemeinsam verschieben (z. B. etwas nach unten)
        householder_group = VGroup(householder1, H1Box)
        householder_group.shift(DOWN*1.5)

        # Zur Szene hinzufügen
        self.add(householder_group)


