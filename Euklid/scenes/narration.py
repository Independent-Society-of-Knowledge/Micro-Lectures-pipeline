from manim import *

class NarrationScene(Scene):
    def __init__(self, text_elements, **kwargs):
        super().__init__(**kwargs)
        self.text_elements = text_elements

    def construct(self):
        for i, element in enumerate(self.text_elements):
            text = Text(element['content'], font="IBM Plex Sans", font_size=24)
            if i == 0:
                self.play(Write(text))
            else:
                self.play(FadeIn(text, shift=UP))
            self.wait(1)