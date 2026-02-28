from manim import *
import random

class HouseholderIntuition(LinearTransformationScene):
    def construct(self):
        plane = self.add_plane(animate=True).add_coordinates
        vector = self.add_vector([-3,-2], color = YELLOW)

        basis = self.get_basis_vectors()
        self.add(basis)
        self.vector_to_coords(vector = vector)
        
        vector2 = self.add_vector([2,3])
        self.write_vector_coordinates(vector = vector2)
        
class Matrix(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=False,
            show_basis_vectors=True
        )
    
    def construct(self):
        matrix = [[-3/5, -4/5],[-4/5, 3/5]]

        matrix_tex = MathTex(
            r"H = \begin{pmatrix}"
            r"-\frac{3}{5} & -\frac{4}{5} \\"
            r"-\frac{4}{5} & \frac{3}{5}"
            r"\end{pmatrix}"
        ).to_edge(UL).add_background_rectangle()

        L = 5
        hyperplane = Line(
            [ L, -2*L, 0],
            [-L,  2*L, 0],
            color=BLUE,
            stroke_width=6
        )

        vect = self.get_vector([3, 4], color=PURPLE_B)

        # 1. Vektor registrieren aber noch nicht transformieren
        self.add_transformable_mobject(vect)
        vect.set_opacity(0)
        
        # 2. Vektor erscheinen lassen
        self.play(vect.animate.set_opacity(1))
        self.wait()

        # 3. Hyperebene erscheint
        self.play(Create(hyperplane),FadeIn(matrix_tex),run_time=2)
        
        self.add_background_mobject(matrix_tex, hyperplane)
        self.wait()

        # 4. Matrix-Transformation
        self.apply_matrix(matrix)
        self.wait()
        self.play(*[FadeOut(mob) for mob in self.mobjects])

class Matrix2(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=False,
            show_basis_vectors=True
        )
    
    def construct(self):
        matrix = [[3/5, 4/5],[4/5, -3/5]]

        matrix_tex = MathTex(
            r"H = \begin{pmatrix}"
            r"\frac{3}{5} & \frac{4}{5} \\"
            r"\frac{4}{5} & -\frac{3}{5}"
            r"\end{pmatrix}"
        ).to_edge(UL).add_background_rectangle()

        L = 5
        hyperplane = Line(
            [-L*4, 2*-L, 0],
            [L*4,  2*L, 0],
            color=BLUE,
            stroke_width=6
        )

        vect = self.get_vector([3, 4], color=PURPLE_B)

        # 1. Vektor registrieren aber noch nicht transformieren
        self.add_transformable_mobject(vect)
        vect.set_opacity(0)
        
        # 2. Vektor erscheinen lassen
        self.play(vect.animate.set_opacity(1),run_time=2)
        self.wait()

        # 3. Hyperebene erscheint
        self.play(Create(hyperplane),FadeIn(matrix_tex),run_time=2)
        
        self.add_background_mobject(matrix_tex, hyperplane)
        self.wait()

        # 4. Matrix-Transformation
        self.apply_matrix(matrix)
        self.wait()
