import numpy as np
import pymunk
from manim import *

DURATION = 12
FPS = 60
SUBSTEPS = 2
FRAME_COUNT = DURATION * FPS + 1
BALL_RADIUS = 0.28
BOX_WIDTH = 13.0
BOX_HEIGHT = 5.8

START_POSITIONS = [
    (-4.8, 1.7),
    (-1.7, 1.2),
    (2.1, 1.8),
    (4.6, 0.1),
    (1.3, -1.7),
    (-2.8, -1.5),
    (0.0, 0.0),
]
START_VELOCITIES = [
    (4.2, 2.4),
    (-3.3, -2.0),
    (2.7, -3.5),
    (-4.0, 2.8),
    (-2.5, 3.6),
    (3.6, -2.4),
    (3.0, 2.0),
]


def build_trajectories():
    space = pymunk.Space()
    space.gravity = (0, 0)
    space.iterations = 80

    half_width = BOX_WIDTH / 2
    half_height = BOX_HEIGHT / 2
    corners = [
        (-half_width, -half_height),
        (half_width, -half_height),
        (half_width, half_height),
        (-half_width, half_height),
    ]
    for index in range(4):
        wall = pymunk.Segment(
            space.static_body,
            corners[index],
            corners[(index + 1) % 4],
            0.03,
        )
        wall.elasticity = 1.0
        wall.friction = 0.0
        space.add(wall)

    bodies = []
    for position, velocity in zip(START_POSITIONS, START_VELOCITIES):
        body = pymunk.Body(1, pymunk.moment_for_circle(1, 0, BALL_RADIUS))
        body.position = position
        body.velocity = velocity
        shape = pymunk.Circle(body, BALL_RADIUS)
        shape.elasticity = 1.0
        shape.friction = 0.0
        space.add(body, shape)
        bodies.append(body)

    trajectories = np.empty((FRAME_COUNT, len(bodies), 2))
    trajectories[0] = [tuple(body.position) for body in bodies]
    for frame in range(1, FRAME_COUNT):
        for _ in range(SUBSTEPS):
            space.step(1 / (FPS * SUBSTEPS))
        trajectories[frame] = [tuple(body.position) for body in bodies]

    return trajectories


def position_at(trajectories, ball_index, time):
    frame = time * FPS
    lower = min(int(frame), FRAME_COUNT - 1)
    upper = min(lower + 1, FRAME_COUNT - 1)
    blend = frame - lower
    return trajectories[lower, ball_index] * (1 - blend) + trajectories[upper, ball_index] * blend


class MultiBallCollision(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        trajectories = build_trajectories()
        clock = ValueTracker(0)

        title = Text("Pymunk + Manim", font_size=36, weight=BOLD, color=BLACK)
        title.to_edge(UP, buff=0.3)
        boundary = Rectangle(
            width=BOX_WIDTH,
            height=BOX_HEIGHT,
            color=BLUE_E,
            stroke_width=3,
        )

        balls = []
        for index in range(len(START_POSITIONS)):
            ball = Circle(
                radius=BALL_RADIUS,
                color=BLACK,
                stroke_width=3,
                fill_opacity=0,
            )
            ball.move_to((*START_POSITIONS[index], 0))

            def update_ball(mobject, ball_index=index):
                point = position_at(trajectories, ball_index, clock.get_value())
                mobject.move_to((point[0], point[1], 0))

            ball.add_updater(update_ball)
            balls.append(ball)

        self.play(Write(title), Create(boundary), run_time=1.2)
        self.play(*(FadeIn(ball, scale=0.5) for ball in balls), run_time=0.6)
        self.play(
            clock.animate.set_value(DURATION),
            run_time=DURATION,
            rate_func=linear,
        )
        self.wait(0.5)
