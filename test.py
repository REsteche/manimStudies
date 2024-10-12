from manim import *

class SquareToCircle(Scene):
    def construct(self):
        square = Square()  # Create a square
        circle = Circle()  # Create a circle

        text = Text("Hello Word!", font_size=72)
        text.to_edge(UP)

        self.play(
            Write(text, run_time=3)
        )

        self.play(
            Create(square), 
            run_time=3
        )  # Animate the creation of the square
        self.wait(1)
        self.play(
            Transform(square, circle),
            run_time=2
        )  # Transform the square into a circle

        self.play(FadeOut(square))  # Fade out the circle

'''
run with: manim -pql test.py SquareToCircle

The -pql flag means “preview” the animation, with “low quality”. 
You can use -qh for high quality.


* Scenes: The core structure where animations happen.
* Mobjects: Basic elements like Square, Circle, Text, etc.
* Animations: Actions applied to mobjects, such as Create, FadeOut, MoveTo, etc.

'''