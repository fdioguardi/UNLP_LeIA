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

        for adj in env.adjacent_positions(position):
            breeze = Breeze(adj)
            things = env.overlapping_with(breeze)
            if things and not any(isinstance(t, Hole) for t in things):
                env.clear(adj)
                env.add_thing(breeze)
