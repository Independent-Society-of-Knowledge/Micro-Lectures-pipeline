from manim import *

class IntroScene(Scene):
    def __init__(self, title, **kwargs):
        super().__init__(**kwargs)
        self.title = title

    def construct(self):
        title = Text(self.title, font="IBM Plex Mono", font_size=40)
        self.play(Write(title))
        self.wait(2)

if __name__ == "__main__":
    intro = IntroScene("Hello World!")
    intro.construct()
