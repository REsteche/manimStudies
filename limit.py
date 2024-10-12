from manim import *

class LimitExplanation(Scene):
    def construct(self):

        # Create Axes
        axes = Axes(
            x_range=[-1, 6], y_range=[-1, 6], 
            x_length=6, y_length=6,
            axis_config={"color": BLUE}
        )
        labels = axes.get_axis_labels(
            x_label="x", 
            y_label="f(x)"
        )

        # Function graph: f(x) = (x-2)/(x-2) when x != 2
        graph = axes.plot(
            lambda x: (x - 2) / (x - 2) if x != 2 else 0, 
            color=GREEN
        )
        graph_label = axes.get_graph_label(
            graph, label="f(x)=\\frac{x-2}{x-2}", 
            x_val=5, 
            direction=UR
        )
        
        # Show a red dot for the limit as x approaches 2
        dot = Dot(
            axes.coords_to_point(2, 1), 
            color=RED
        )
        dot_label = MathTex(r"\lim_{x \to 2} f(x)").next_to(dot, UP)
        
        # Play animations
        self.play(
            Create(axes), 
            Write(labels), 
            run_time=3
        )
        self.play(
            Create(graph), 
            Write(graph_label)
        )
        self.play(
            FadeIn(dot), 
            Write(dot_label)
        )

        self.wait(2)

'''
run with: manim -pql limit.py LimitExplanation

A limit describes how a function behaves as the input approaches a certain value. 
We can represent this graphically by showing a curve and the behavior of the function near a point.
'''