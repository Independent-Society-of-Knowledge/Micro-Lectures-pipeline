from manim import *

class EquationScene(Scene):
    def __init__(self, equation, **kwargs):
        super().__init__(**kwargs)
        self.equation = equation

    def construct(self):
        eq = MathTex(self.equation)
        self.play(Write(eq))
        self.wait(2)