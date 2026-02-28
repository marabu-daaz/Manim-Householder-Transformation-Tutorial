from manim import*
import math
import numpy as np
class Householder(VectorScene):
    def construct(self):
        # #graph
        # axes = Axes(x_range = [-3,3,1], y_range = [-3,3,1], 
        # x_length=6, y_length=6)

        #plane
        plane = NumberPlane(background_line_style={"stroke_opacity": 0.5})
        
        #Einheitsnormale
        a,b = 1/math.sqrt(2), -1/math.sqrt(2)
        v_vec = np.array([a,b,0])
        v = Arrow(start=ORIGIN, end=[a, b, 0], color=YELLOW, buff=0)
        label = MathTex(r"\vec{v}")
        label.next_to(v.get_end(),RIGHT)
        
        #vektor x
        x_vec = np.array([3,0,0])
        x = Arrow(start = ORIGIN, end= [3,0,0], color = GREEN,  buff = 0)
        xlabel = MathTex(r"\vec{x}")
        xlabel.add_updater(lambda m: m.next_to(x.get_end(), UP))

        #vektor x schlange
        xs = Arrow(start = ORIGIN, end= [0,3,0], color = GREEN,  buff = 0)
        xslabel = MathTex(r"\vec{x}'")
        xslabel.add_updater(lambda s: s.next_to(xs.get_end(), LEFT + DOWN * 0.3))

        #Dashed Line
        dashed = DashedLine(x.get_end(), xs.get_end(), color=GREY)

        #Hyperebene
        dx, dy = -b, a
        L = 5.6  

        hyperplane = Line(
            [-L*dx, -L*dy, 0],
            [ L*dx,  L*dy, 0],
            color=BLUE
        )
        hyperplane.set_stroke(width=6)
        line_label = MathTex("Hyperplane")
        line_label.move_to(hyperplane.get_end() + DOWN + RIGHT * 1.2)

        #Skalarprodukt aus v und x
        dot = np.dot(v_vec, x_vec)      
        proj = dot * v_vec
        dotproduct = DashedLine(ORIGIN, proj, color = RED)

        #dashed
        dash = DashedLine(x.get_end(), proj, color = GREY)

        #Skalarlabel
        slabel = MathTex(r"v^\top x",  color = RED)
        slabel.next_to(dotproduct.get_end(), buff=0.2)

        #vTxv
        p_vec = Arrow(ORIGIN, -proj, color =RED, buff = 0)
        p_vec_label = MathTex(r"-(v^\top x)v", color = RED).next_to(p_vec.get_end(), LEFT)
        

        #proj1
        foot = x_vec - proj
        p1 = Arrow(x.get_end(), foot, color = ORANGE, buff=0)
        p1_label = MathTex(r"-(v^\top x)v", color = ORANGE).next_to(p1.get_center(), UR)

        #proj2
        p2 = Arrow(foot, xs.get_end(), color = ORANGE, buff=0)
        p2_label = MathTex(r"-(v^\top x)v", color = ORANGE).next_to(p2.get_center(), UP * 1.5 + RIGHT * 0.3)

        #Formel
        formula = MathTex(
            "x", r"-2v^\top x v"
        ).to_edge(UL* 1.4)
        box = SurroundingRectangle(
            formula,
            color=BLUE,
            buff=0.5,
            stroke_width=4, 
            fill_color=BLACK,
            fill_opacity=1.0
        )
        #derived Formel
        formula1 = MathTex(
            r"(I - 2v v^\top )x"
        ).to_edge(UP * 1.3 + RIGHT)

        #Householderformel mit Boxen
        householder = MathTex(
            r"H = I - 2 v v^T \phantom{\frac{}{v^T v}}"
        ).to_edge(UP*8+LEFT*2)

        householder1 = MathTex(
            "H", "=", "I", "-", r"\frac{2 v v^T}{v^T v}"
        ).to_edge(UL * 2)

        HBox = SurroundingRectangle(householder, color=BLUE, buff=0.25)
        H1Box = SurroundingRectangle(householder1, color=RED, buff=0.25)

        #EigeschaftenText
        orthogonal = Text("Die Matrix ist symmetrisch")


        #Group Scene
        scene_group = VGroup(plane, x, xs, v, dashed, hyperplane, label, xslabel, xlabel, 
        line_label, p1, p2, p_vec, p_vec_label, p1_label, p2_label, box, formula)
        text = MathTex(r"x' = x-2v^Txv").to_corner(UP + RIGHT* 1.8, buff= 1)
        text1 = MathTex(r"x' = (I - 2vv^T)x").to_corner(UP* 2 + RIGHT* 1.8, buff= 1)
        text2 = MathTex(r"\Rightarrow", r"H = I - 2v v^T").to_corner(UP*3 + RIGHT* 1.8, buff= 1)
        
        # text1 = MathTex(r"\text{Herleitung } H = I - 2 \frac{v v^T}{v^T v}").to_corner(UR, buff= 1)

        #Animations
        self.play(FadeIn(plane), run_time=5)
        self.wait(3)
        self.play(GrowArrow(v), run_time=2)
        self.play(Write(label))
        self.wait(2)
        self.play(Create(hyperplane), Write(line_label), run_time=2)
        self.wait(4.5)
        self.play(GrowArrow(x))
        self.play(Write(xlabel))
        self.wait(4)
        self.play(TransformFromCopy(x,xs), run_time=2)
        self.play(Write(xslabel))
        self.play(Create(dashed), run_time=2)
        self.wait(7)
        parrow = Arrow(start=ORIGIN, end=proj, color=RED, buff=0)
        self.play(TransformFromCopy(x,parrow))
        self.wait(4)
        self.play(FadeOut(parrow))
        self.play(Create(dotproduct), Write(slabel), Create(dash))
        self.wait(2)
        self.play(Indicate(dotproduct, scale_factor = 1.4 , color=RED))
        self.wait(7)
        self.play(TransformFromCopy(v, p_vec), Write(p_vec_label), run_time = 2)
        self.wait(4)
        self.play(Indicate(p_vec, scale_factor = 1.2, color=RED))
        self.wait(4)
        self.play(TransformFromCopy(p_vec, p1), Transform(p_vec, p2) , TransformFromCopy(p_vec_label, p1_label), Transform(p_vec_label, p2_label),
        FadeOut(dotproduct, slabel, dash))
        self.play(Create(box))
        self.play(Indicate(x, scale_factor = 1.2))
        self.play(FadeIn(formula[0]))
        self.play(Indicate(p1, scale_factor = 1.2))
        self.wait()
        self.play(Indicate(p2, scale_factor = 1.2))
        self.play(FadeIn(formula[1]))
        self.wait(3)
        self.play(Indicate(formula), Indicate(xs))
        # self.play(Transform(formula, formula1))
        self.wait(2)
        self.play(scene_group.animate.scale(0.4).to_corner(UL))
        self.wait(2)
        self.play(Write(text), run_time=2)
        self.wait(7)
        self.play(Write(text1), run_time=2)
        self.wait(6)
        self.play(Write(text2), run_time=2)
        self.wait(4)
        self.play(scene_group.animate.shift(8*LEFT),text.animate.shift(8*RIGHT), text1.animate.shift(8*RIGHT), text2.animate.shift(8*RIGHT),  run_time = 2)
        self.remove(scene_group, text, text1, text2)
        self.play(Create(HBox), Create(H1Box), Create(householder), Create(householder1))
        self.wait(6)

        title = Tex("Householder-Matrix: Eigenschaften").to_edge(UR*1.9)
        self.wait(7)

        props = VGroup(
            MathTex(r"1.\;\; H^T = H \quad \text{(symmetrisch)}"),
            MathTex(r"2.\;\; H^T H = I \quad \text{(orthogonal)}"),
            MathTex(r"3.\;\; H^{-1} = H \quad \text{(selbstinvers)}")
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)

        props.next_to(title, DOWN, buff=0.6)

        # Titel + Definition
        self.play(Write(title))
        self.wait(3)

        #Eigenschaften nacheinander
        for p in props:
            self.play(Write(p))
            self.wait(5)

        self.wait(5)
        self.play(FadeOut(props, HBox, householder, title), householder1.animate.move_to(ORIGIN), H1Box.animate.move_to(ORIGIN), run_time=3)
        self.wait(10)
        self.play(FadeOut(H1Box, householder1))
        self.wait(2)

class Comparison(Scene):
    def construct(self):
        def small_arrow(start, end, color, stroke_width=3):
            return Arrow(
                start, end, buff=0, color=color,
                stroke_width=stroke_width,
                tip_length=0.15,
                max_tip_length_to_length_ratio=0.1
            )

        # Linke Seite - Plus Fall
        left_plane = NumberPlane(
            x_range=[-6,6,1], y_range=[-5,5,1],
            x_length=5, y_length=3.5,
            background_line_style={"stroke_opacity": 0.25}
        ).shift(LEFT * 3.5)
        
        left_hyper = Line(
            left_plane.c2p(-1.2*2, 2.4*2), left_plane.c2p(1.2*2, -2.4*2),
            color=BLUE, stroke_width=3
        )
        
        left_normal = small_arrow(left_plane.c2p(0,0), left_plane.c2p(4,2), YELLOW)
        left_normal_label = MathTex(r"\vec{v}", font_size=24, color=YELLOW).next_to(left_normal.get_end(), RIGHT, buff=0.08)

        left_vec_x = small_arrow(left_plane.c2p(0,0), left_plane.c2p(3,4), GREEN)
        left_vec_x_label = MathTex(r"\vec{x}", font_size=24, color=GREEN).next_to(left_vec_x.get_end(), UR, buff=0.08)

        left_vec_result = small_arrow(left_plane.c2p(0,0), left_plane.c2p(-5,0), GREEN)
        left_result_label = MathTex(r"\vec{x}'", font_size=24, color=GREEN).next_to(left_vec_result.get_end(), DOWN, buff=0.08)

        left_label = MathTex("v = x + \\|x\\| e_1", font_size=28).next_to(left_plane, UP, buff=0.15)
        
        left_group = VGroup(left_plane, left_hyper, left_normal, left_normal_label,
            left_vec_x, left_vec_x_label, left_vec_result, left_result_label, left_label)
        left_box = SurroundingRectangle(left_group, color=BLUE, buff=0.15, stroke_width=2)

        # Rechte Seite - Minus Fall
        right_plane = NumberPlane(
            x_range=[-6,6,1], y_range=[-5,5,1],
            x_length=5, y_length=3.5,
            background_line_style={"stroke_opacity": 0.25}
        ).shift(RIGHT * 3.5)
        
        right_hyper = Line(
            right_plane.c2p(-4*1.5, -2*1.5), right_plane.c2p(4*1.5, 2*1.5),
            color=BLUE, stroke_width=3
        )

        right_normal = small_arrow(right_plane.c2p(0,0), right_plane.c2p(-2,4), YELLOW)
        right_normal_label = MathTex(r"\vec{v}", font_size=24, color=YELLOW).next_to(right_normal.get_end(), LEFT, buff=0.08)

        right_vec_x = small_arrow(right_plane.c2p(0,0), right_plane.c2p(3,4), GREEN)
        right_vec_x_label = MathTex(r"\vec{x}", font_size=24, color=GREEN).next_to(right_vec_x.get_end(), UR, buff=0.08)

        right_vec_result = small_arrow(right_plane.c2p(0,0), right_plane.c2p(5,0), GREEN)
        right_result_label = MathTex(r"\vec{x}'", font_size=24, color=GREEN).next_to(right_vec_result.get_end(), DOWN, buff=0.08)

        right_label = MathTex("v = x - \\|x\\| e_1", font_size=28).next_to(right_plane, UP, buff=0.15)
        
        right_group = VGroup(right_plane, right_hyper, right_normal, right_normal_label,
            right_vec_x, right_vec_x_label, right_vec_result, right_result_label, right_label)
        right_box = SurroundingRectangle(right_group, color=RED, buff=0.15, stroke_width=2)

        # Einblenden
        self.play(
            FadeIn(left_plane), Create(left_hyper),
            GrowArrow(left_vec_x), Write(left_vec_x_label),
            GrowArrow(left_vec_result), Write(left_result_label),
            GrowArrow(left_normal), Write(left_normal_label),
            Write(left_label), Create(left_box),
            FadeIn(right_plane), Create(right_hyper),
            GrowArrow(right_vec_x), Write(right_vec_x_label),
            GrowArrow(right_vec_result), Write(right_result_label),
            GrowArrow(right_normal), Write(right_normal_label),
            Write(right_label), Create(right_box),
            run_time=3
        )
        self.wait(8)
        self.play(Indicate(left_label),Indicate(right_label), run_time=2)
        self.play(Indicate(right_normal),Indicate(left_normal), run_time=2)
        self.wait(4)