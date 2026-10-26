from manim import *


class EnvCheck(Scene):
    def construct(self):
        title = Text("Manim 环境测试", font_size=48)
        formula = MathTex(r"e^{i\pi} + 1 = 0", font_size=60)
        group = VGroup(title, formula).arrange(DOWN, buff=0.8)

        self.play(Write(title))
        self.play(TransformFromCopy(title, formula))
        self.wait()
        circle = Circle(radius=1.2, color=BLUE).surround(formula)
        self.play(Create(circle))
        self.play(FadeOut(group), FadeOut(circle))
