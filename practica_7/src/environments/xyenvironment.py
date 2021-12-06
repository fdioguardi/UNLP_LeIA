from __future__ import annotations
import random
from typing import TYPE_CHECKING

from ..positions import Point

from .environment import Environment

if TYPE_CHECKING:
    from ..agents import Agent
    from ..positions import Position
    from ..things import Thing


class XYEnvironment(Environment):
    """
    Environment that simulates a 2D plane.

    Attributes:
        agent (Agent): agent in the environment.
        start (Point): starting point of the plane.
        things (list[Thing]): list of things in the environment.
        height (int): height of the plane.
        width (int): width of the plane.
    """

    def __init__(
        self, agent: Agent, width: int = 10, height: int = 10
    ) -> None:
        """
        Initialize an XYEnvironment.

        :param agent: agent to add to the environment.
        :param width: width of the plane.
        :param height: height of the plane.
        """
        super().__init__(agent)
        self.width: int = width
        self.height: int = height
        self.start: Point = Point(0, 0)

    def add_thing(self, thing: Thing) -> Thing:
        """
        Add a thing to the environment.

        :param thing: thing to add to the environment.
        :return: the thing to be added to the environment.
        """
        self.things.append(thing)

        return thing

    def remove_thing(self, thing: Thing) -> None:
        """
        Remove a thing from the environment.

        :param thing: thing to remove from the environment.
        """

        if thing in self.things:
            self.things.remove(thing)

    def random_location_inbounds(self):
        """
        Returns a random location that is inbounds

        :return: a point inbounds of the environment.
        """

        return Point(
            random.randint(self.start.x, self.width - 1),
            random.randint(self.start.y, self.height - 1),
        )

    def in_bounds(self, position: Position) -> bool:
        """
        Returns True if the position is inbounds.

        :param position: position to check.
        :return: True if the position is inbounds.
        """

        return (
            position.x >= self.start.x
            and position.x < self.width
            and position.y >= self.start.y
            and position.y < self.height
        )

    def adjacent_positions(self, position: Position) -> list:
        """
        Returns a list of positions adjacent to the given position.

        :param position: position to get adjacent positions for.
        :return: A list of positions adjacent to the given position.
        """

        adjacent_positions = [
            Point(position.x + 1, position.y),
            Point(position.x - 1, position.y),
            Point(position.x, position.y + 1),
            Point(position.x, position.y - 1),
        ]

        return [
            adjacent_position
            for adjacent_position in adjacent_positions
            if self.in_bounds(adjacent_position)
        ]

    def graphic_map(self):
        map = [[" " for _ in range(self.width)] for _ in range(self.height)]
        for thing in self.things:
            map[thing.position.x][thing.position.y] = thing.graphic()
        map[self.agent.position.x][self.agent.position.y] = "A"
        for row in map:
            print(row)