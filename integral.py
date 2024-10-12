from manim import *

class IntegralExplanation(Scene):
    def construct(self):
        # Create Axes
        axes = Axes(
            x_range=[-1, 6], y_range=[-1, 25], 
            x_length=6, y_length=6,
            axis_config={"color": BLUE}
        )
        labels = axes.get_axis_labels(x_label="x", y_label="f(x)")

        # Graph of f(x) = x^2
        graph = axes.plot(lambda x: x ** 2, color=GREEN)
        graph_label = axes.get_graph_label(
            graph, label="f(x)=x^2", 
            x_val=5, 
            direction=UR
        )

        # Area under curve between x=1 and x=4
        area = axes.get_area(
            graph, 
            x_range=[1, 3], 
            color=BLUE, 
            opacity=0.5
            )
        area_label = MathTex(r"\int_1^3 x^2 dx").next_to(area, UP)

        # Play animations
        self.play(
            Create(axes), 
            Write(labels),
            run_time=2
        )
        self.play(
            Create(graph), 
            Write(graph_label),
            run_time=2
        )
        self.play(
            Create(area), 
            Write(area_label)
        )
        self.wait(2)


'''
run with: manim -pql integral.py IntegralExplanation

The derivative measures the rate of change of a function,
or in other words, the slope of the tangent line to a curve at a specific point.
'''