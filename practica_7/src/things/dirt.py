from __future__ import annotations
from typing import TYPE_CHECKING

from .thing import Thing

if TYPE_CHECKING:
    from ..positions import Position


class Dirt(Thing):
    """
    Dirt is a thing that can be placed on the floor.

    Attributes:
        position (Position): The position of the dirt.
    """

    def __init__(self, position: Position) -> None:
        """
        Initialize a dirt object.

        :param position: The position of the dirt.
        """

        self.position = position

    def graphic(self) -> str:
        """
        Returns the Dirt's representation.

        :return: the string representing dirt.
        """
        return "*"
