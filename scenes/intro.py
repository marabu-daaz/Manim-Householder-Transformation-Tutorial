from manim import *

class Intro(Scene):
    def construct(self):
    
        text = Text("Householder Transformation" , font_size= 72).to_edge(UP)
        img = ImageMobject("assets/house.png")
        
        qr = Text("QR-Faktorisierung", font_size=60).to_edge(UP)
        #a=qr
        aqr = MathTex("A", "=", "Q", "R", font_size=90)
        # Matrix A
        A = Matrix([[3,1,0],
                    [4,2,1],
                    [0,1,2]])
        A_label = Text("A").next_to(A, UP, buff=0.4)

        Q = Matrix([])
        Q_label = Text("Q")

        
        # Highlighting zero entries
        R = Matrix([
            ["*", "*", "*"],
            ["0", "*", "*"],
            ["0", "0", "*"]
        ])
        R_label = Text("R").next_to(R, UP, buff=0.4)
        R_label.add_updater(lambda x: x.next_to(R, UP, buff= 0.4))
        entries = R.get_entries()
        n = 3
        below_diag = []

        for r in range(n):
            for c in range(n):
                if r > c:          
                    below_diag.append(entries[r*n + c])

        # Mini-Koordinatensystem
        mini_plane = NumberPlane(
            x_range=[-3,3,1],
            y_range=[-3,3,1],
            x_length=4,
            y_length=4,
            background_line_style={"stroke_opacity": 0.4}
        )

        # Fixe Box
        box = SurroundingRectangle(mini_plane, buff=0.3, color=WHITE)

        # Alles zusammen
        ortho_demo = Group(mini_plane, box).scale(0.7)
        ortho_demo.to_corner(DOWN*2+LEFT*5.5)


        # Animations
        self.play(Write(text), FadeIn(img), run_time =3)
        self.play(FadeOut(text), FadeOut(img))
        self.remove(text)
        for idx, part in enumerate(aqr):
            self.play(Write(part))
            if idx == 2:   # Q
                continue
            elif idx == 3:
                break
            self.wait(1.6)
            

        self.play(aqr.animate.shift(UP*3))
        # self.play(Write(A), Write(A_label), Write(qr))
        self.wait(2)
        # --- Text für Q ---
        Q_anchor = aqr[2]   # das Q in A = Q R
        Q_text = Text("orthogonal")
        Q_text.next_to(Q_anchor, DOWN*0.9 + LEFT, buff=1.2)

        Q_line = Line(
            Q_anchor.get_bottom(),
            Q_text.get_top(),
            stroke_width=8,
            buff=0.25
        )

        # --- Text für R ---
        R_anchor = aqr[3]   # das R in A = Q R
        R_text = Text("upper triangular")
        R_text.next_to(R_anchor, DOWN*0.9 + RIGHT*0.1, buff=1.2)

        R_line = Line(
            R_anchor.get_bottom(),
            R_text.get_top(),
            stroke_width=8,
            buff=0.4
        )

        #Entenimage
        ente = SVGMobject("assets/ente.svg")
        ente.scale(0.35)
        ente.move_to(mini_plane.c2p(0, 0))  # Position auf der Plane
        self.play(Create(Q_line), Write(Q_text), FadeIn(ortho_demo), FadeIn(ente))
        for _ in range(4):
            self.play(
                Rotate(ente, angle=-PI/2, about_point=ente.get_center()),
                run_time=1.5
            )
            self.wait(0.8)
        self.wait(2)
        self.play(Create(R_line), Write(R_text))
        self.wait(2)
        self.play(FadeOut(Q_line,Q_text,R_line,R_text, ente, mini_plane, ortho_demo))
        self.remove(Q_line,Q_text,R_line,R_text, ente, ortho_demo)
        self.wait()
        self.play(TransformFromCopy(aqr[3], R))
        self.wait(1.7)
        self.play(
            AnimationGroup(*[
                Indicate(e, color=YELLOW, scale_factor=1.4)
                for e in below_diag
            ])
        )
        self.play(FadeOut(R, aqr), run_time=2)
        
        #Householder definition

        C = Matrix([
            [1, 3, 1],
            [2, 2, 2],
            [2, 4, 5]
        ])

        R_values = [
            ["3", "5", "5"],
            ["0", "2", "1"],
            ["0", "0", "2"]
        ]

        self.add(C)
        
        ente.shift(2*LEFT+DOWN)
        self.play(FadeIn(C), FadeIn(ente))
        self.wait(1)

        entries = C.get_entries()
        n = 3

        box = SurroundingRectangle(entries[0], color=YELLOW, buff=0.1)
        self.play(Create(box))

        for r in range(n):
            for c in range(n):
                idx = r * n + c
                current_entry = entries[idx]
                target_val = R_values[r][c]

                if idx != 0:
                    self.play(box.animate.move_to(current_entry), run_time=0.3)

                new_val = MathTex(target_val).move_to(current_entry)

                if r > c:
                    new_val.set_color(BLUE)
                else:
                    new_val.set_color(WHITE)

                self.play(
                    FadeOut(current_entry, shift=UP * 0.3),
                    FadeIn(new_val, shift=UP * 0.3),
                    run_time=0.5
                )
                entries[idx] = new_val
                self.wait(0.1)

        text = Text("Householder Transformation" , font_size= 60).to_edge(UP)   
        self.play(FadeOut(box), Create(text), run_time=2)
        
       
        # Matrix einfärben, um das Ergebnis zu betonen
        self.play(C.animate.set_color(WHITE))
    
        self.play(
            FadeOut(C.get_brackets()),
            *[FadeOut(entries[i]) for i in range(n * n)], FadeOut(ente),FadeOut(text)
        )


class FormulaApplication(Scene):
    def construct(self):

        # Matrix n kreuz n
        B = Matrix([[3,1],
                   [4,3]])
        B_label = Text("B").next_to(B, UP, buff=0.4)

        col = B.get_columns()[0]
        vec = Matrix([[3],[4]])

        #plane
        plane = NumberPlane(
        x_range=[-8,8,1],
        y_range=[-6,6,1],
        x_length=14,
        y_length=10,
        background_line_style={"stroke_opacity": 0.5})
        
        #vektorx
        x  = Arrow(plane.c2p(0,0), plane.c2p(3,4), buff=0, color=GREEN)
        x_label = MathTex(r"\vec{x}", font_size=70).next_to(x.get_end(), UR, buff=0.2)

        #vektorx'
        xs = Arrow(plane.c2p(0,0), plane.c2p(5,0), buff=0, color=RED)
        xs_label = Matrix([[5],[0]]).scale(0.7).next_to(xs.get_end(), UR, buff=0.2)

        #Einheitsvektor Formel PLUS
        formula = MathTex(
            "v", "=", "x", "+", r"\|x\|", "e_1",
            font_size=70
        )
        formula.to_edge(UP + LEFT)

        #Einheitsvektor Formel MINUS
        formula1 = MathTex(
            "v", "=", "x", "-", r"\|x\|", "e_1",
            font_size=70
        )
        formula1.to_edge(UP + LEFT)

        # PLUS Fall
        plus = MathTex("+").move_to(formula[3])
        
        # MINUS Fall
        minus = MathTex("-").move_to(formula[3])
        
        #e1
        e1 = Arrow(plane.c2p(0, 0), plane.c2p(1, 0), buff=0, color=RED, stroke_width=8)
        e1_label = MathTex("e_1", font_size=70).next_to(e1.get_end(), DOWN, buff=0.15)

        #skaliertes e1
        scaled_e1 = Arrow(plane.c2p(0, 0), plane.c2p(5, 0), buff=0, color=RED, stroke_width=8)
        scaled_e1_label = MathTex(r"\|x\| e_1", font_size=70).next_to(scaled_e1.get_end(), DOWN *2, buff=0.15)
        
        #Summenvektor
        a,b = 8,4
        sum_vec = Arrow(plane.c2p(0,0), plane.c2p(a,b), buff=0,
        color=YELLOW, stroke_width=8)
        sum_label = MathTex(r"\vec{v}", font_size=70).next_to(sum_vec.get_end(), DOWN*5+LEFT*4 , buff=0.2)

        #Hyperplane
        #Line
        dx, dy = -b, a
        L = 1
        hyperplane1 = Line([dx*-L, dy*-L, 0],[dx*L, dy*L, 0], color=BLUE, stroke_width=7)
        hyperlane1_label = MathTex("Hyperplane").next_to(hyperplane1.get_center(), LEFT*4 + UP*3)

        #Spiegelvektor1
        x1s = Arrow(plane.c2p(0,0), plane.c2p(-5,0), buff=0, color=GREEN)
        x1s_label = Matrix([[-5],[0]]).scale(1).next_to(x1s.get_end(), LEFT + UP)

        #negierter vektor nachdem e1 skaliert wurde
        neg_scaled_e1 = Arrow(plane.c2p(0, 0), plane.c2p(-5, 0), buff=0, color=RED, stroke_width=8)
        neg_scaled_e1_label = MathTex(r"-\|x\| e_1", font_size=70).next_to(neg_scaled_e1.get_end(), DOWN*2, buff=0.15)

        #Differenzenvektor
        v_minus = Arrow(plane.c2p(0,0), plane.c2p(-2,4), buff=0, color=YELLOW, stroke_width=8)
        v_minus_label = MathTex(r"\vec{v}", font_size=70).next_to(v_minus.get_end(), DOWN*4+ LEFT, buff=0.2)


        # Animations
        self.play(Create(B), Write(B_label), run_time=2)
        self.wait(5)
        
        self.play(TransformFromCopy(col, vec), FadeOut(B), FadeOut(B_label))
        self.play(FadeIn(plane), vec.animate.shift(RIGHT*3.6 + UP*3), run_time=3)
        self.play(Create(x))
        #self.play(TransformFromCopy(x, xs), run_time=2)
        #self.play(Write(xs_label))
        self.wait(4)
        self.play(Write(formula))
        
        #self.play(Indicate(formula[3], color=RED))
        self.wait(4)
        #self.play(ReplacementTransform(formula[3], minus))
        #self.play(Indicate(minus, color=BLUE))
        #self.wait()
        #x indication
        self.play(Indicate(formula[2], color=GREEN, scale_factor=1.15))
        self.play(Indicate(x, color=GREEN, scale_factor=1.05))
        self.wait(2)
        #e1 einblenden und indicaten
        self.play(Indicate(formula[5], color=RED, scale_factor=1.15))
        self.play(FadeIn(e1))
        self.wait(2)
        
        #Norm skalieren
        self.play(Indicate(formula[4], scale_factor=1.15))
        self.play(Transform(e1, scaled_e1), Transform(e1_label, scaled_e1_label), run_time=3)
        self.play(Indicate(formula[3], scale_factor=1.3))
        self.wait(6)
        #Vektoren addieren
        self.play(e1.animate.shift(x.get_end()), FadeOut(e1_label), FadeOut(vec))
        self.wait(2)
        #Summenvektor erstellen
        self.play(Create(sum_vec), Create(sum_label))
        self.play(FadeOut(e1))
        self.remove(e1)
        self.wait(2)
        #Hyperebene erschaffen
        
        self.play(FadeIn(hyperplane1), FadeIn(hyperlane1_label), run_time=2)
        self.wait(2)
        self.play(TransformFromCopy(x, x1s), FadeIn(x1s_label), run_time=2)
        self.wait(9)
        self.play(FadeOut(hyperplane1), FadeOut(hyperlane1_label), 
        FadeOut(sum_vec), FadeOut(x1s), FadeOut(x1s_label), FadeOut(sum_label))
        #vielleicht neue Scene fuer uebersichtlichkeit
        
        self.play(Transform(formula, formula1))
        #e1 einblenden und indicaten
        self.play(Indicate(formula[5], color=RED, scale_factor=1.15))
        e1 = Arrow(plane.c2p(0, 0), plane.c2p(1, 0), buff=0, color=RED, stroke_width=8)
        e1_label = MathTex("e_1", font_size=70).next_to(e1.get_end(), DOWN, buff=0.15)
        self.play(FadeIn(e1_label), FadeIn(e1))
        self.wait(2)
        #Norm skalieren
        self.play(Indicate(formula[4], scale_factor=1.15))
        self.play(Transform(e1, scaled_e1), Transform(e1_label, scaled_e1_label), run_time=3)
        self.play(Indicate(formula[3], scale_factor=1.3))
        self.wait(1)
        #subtraktion
        self.play(Transform(e1, neg_scaled_e1), Transform(e1_label, neg_scaled_e1_label), run_time=2)
        self.play(e1.animate.shift(x.get_end()), FadeOut(e1_label), run_time=1.5)
        #Ergebnisvektor zeigen
        self.play(Create(v_minus), FadeIn(v_minus_label))
        self.wait(1)
        
        a2, b2 = -2, 4
        dx2, dy2 = -b2, a2  # (-4, -2)

        L = 8
        hyper2 = Line(plane.c2p(-L*dx2, -L*dy2), plane.c2p(L*dx2, L*dy2), color=BLUE, stroke_width=7)
        hyper2_label = Text("Hyperplane", font_size=36).next_to(hyper2, LEFT, buff=0.3)
        self.play(FadeOut(e1))
        self.play(FadeIn(hyper2), FadeIn(hyper2_label), run_time=2)
        self.wait(1)
        xs2 = Arrow(plane.c2p(0,0), plane.c2p(5,0), buff=0, color=GREEN, stroke_width=8)
        xs2_label = Matrix([[5],[0]]).scale(1).next_to(xs2.get_end(), RIGHT + UP)
        
        self.play(TransformFromCopy(x, xs2), FadeIn(xs2_label))
        self.wait(7)
        return
        