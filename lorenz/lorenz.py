from manimlib import *

from scipy.integrate import odeint
from scipy.integrate import solve_ivp
import numpy as np

from manimlib.mobject.types.dot_cloud import GlowDot
from manimlib.mobject.changing import TracingTail
from manimlib.animation.creation import ShowCreation

from manimlib.constants import FRAME_WIDTH

def lorenz_system(t, state, sigma=10, rho=28, beta=8 / 3):
    x, y, z = state
    dxdt = sigma * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z
    return [dxdt, dydt, dzdt]


def ode_solution_points(function, state0, time, dt=0.01):
    solution = solve_ivp(
        function,
        t_span=(0, time),
        y0=state0,
        t_eval=np.arange(0, time, dt)
    )
    return solution.y.T


def for_later():
    tail = VGroup(
        TracingTail(dot, time_traced=3).match_color(dot)
        for dot in dots
    )


class LorenzAttractor(Scene):
    def construct(self):
        # Set up axes
        axes = ThreeDAxes(
            x_range=(-50, 50, 5),
            y_range=(-50, 50, 5),
            z_range=(-0, 50, 5),
            width=16,
            height=16,
            depth=8,
        )
        axes.set_width(FRAME_WIDTH)
        axes.center()

        self.frame.reorient(43, 76, 1, IN, 10)
        self.frame.add_updater(lambda m, dt: m.increment_theta(dt * 3 * DEGREES))
        self.add(axes)

        # Add the equations
        equations = Tex(
            R"""
            \begin{aligned}
            \frac{\mathrm{d} x}{\mathrm{~d} t} & =\sigma(y-x) \\
            \frac{\mathrm{d} y}{\mathrm{~d} t} & =x(\rho-z)-y \\
            \frac{\mathrm{d} z}{\mathrm{~d} t} & =x y-\beta z
            \end{aligned}
            """,
            t2c={
                "x": RED,
                "y": GREEN,
                "z": BLUE,
            },
            font_size=30
        )
        equations.fix_in_frame()
        equations.to_corner(UL)
        equations.set_backstroke()
        self.play(Write(equations))
        

        # Compute a set of solutions
        epsilon = 1e-5
        evolution_time = 30
        n_points = 10
        states = [
            [10, 10, 10 + n * epsilon]
            for n in range(n_points)
        ]
        colors = color_gradient([BLUE_E, BLUE_A], len(states))

        curves = VGroup()
        for state, color in zip(states, colors):
            points = ode_solution_points(lorenz_system, state, evolution_time)
            curve = VMobject().set_points_smoothly(axes.c2p(*points.T))
            curve.set_stroke(color, 1, opacity=0.25)
            curves.add(curve)

        curves.set_stroke(width=2, opacity=1)

        # Display dots moving along those trajectories
        dots = Group(GlowDot(color=color, radius=0.25) for color in colors)

        def update_dots(dots, curves=curves):
            for dot, curve in zip(dots, curves):
                dot.move_to(curve.get_end())

        dots.add_updater(update_dots)

        tail = VGroup(
            TracingTail(dot, time_traced=3).match_color(dot)
            for dot in dots
        )

        self.add(dots)
        self.add(tail)
        curves.set_opacity(0)
        self.play(
            *(
                ShowCreation(curve, rate_func=linear)
                for curve in curves
            ),
            run_time=evolution_time,
        )

"""
ctrl + alt + T (terminal as new windown)

ALWAYS remeber that for that workflow to function you'll need to use 

from manimlib import * (grants version)

instead of

from manim import * (community version)


to work on that script, prioritize sharing the screen in thre blocks.

> left half of the screen: the text editor you use to code (can be sublime, vs code, etc)

> the right down corner of the screen:  open a terminal (ctrl + alt + T)
and go to the exact path of your script and run the following command:

manimgl lorenz.py LorenzAttractor -se 119

> the right up corner of the screen: the output of the command above
will be displayed here as an interaction Scene displayer for you to work with.

> to get the code running you need to copy the code and run in the terminal

$ checkpoint_paste() # I'll probably create a shortcut in the vs code for that in the future
"""

class EndScreen():
    pass