from __future__ import annotations
from typing import TYPE_CHECKING

from .thing import Thing
from .breeze import Breeze

if TYPE_CHECKING:
    from ..positions import Position
    from ..environments import Environment


class Hole(Thing):
    """
    Hole is an obstacle that can exist in an environment.

    Attributes:
        position (Position): The position of the hole.
    """

    def __init__(self, position: Position, env: Environment) -> None:
        """
        Initialize a Hole object. Create Breeze objects in the positions
        adjacent to the Hole.

        :param position: The position of the Hole.
        :param env: The environment in which the Hole is in.
        """

        self.position = position

        if env.things_in_position(position):
            env.clear(position)

        for adj in env.adjacent_positions(position):
            things = env.things_in_position(adj)
            if not any(isinstance(t, Hole) or isinstance(t, Breeze) for t in things):
                env.add_thing(Breeze(adj))

    def graphic(self):
        return "o"