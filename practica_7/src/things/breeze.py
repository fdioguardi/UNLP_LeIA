from __future__ import annotations
from typing import TYPE_CHECKING

from .thing import Thing

if TYPE_CHECKING:
    from ..positions import Position


class Breeze(Thing):
    """
    Breeze is an indicator that there's a Hole in the proximity.

    Attributes:
        position (Position): The position of the breeze.
    """

    def __init__(self, position: Position) -> None:
        """
        Initialize a breeze object.

        :param position: The position of the dirt.
        """

        self.position = position
