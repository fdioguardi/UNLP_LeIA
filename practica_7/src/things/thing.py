from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..positions import Position


class Thing:
    """
    A thing is a physical object that can be placed in an environment.

    Attributes:
        position (Position): The position of the thing.
    """

    def __init__(self, position: Position):
        """
        Initialize a thing.

        :param position: The position of the thing.
        """
        self.position = position

    def overlaps(self, other: Thing) -> bool:
        """
        Returns True if this thing overlaps with another thing.
        Overlapping is defined as the same position.

        :param other: The other thing.
        :return: True if the two things overlap, False otherwise.
        """

        return self.position == other.position

    def graphic(self):
        raise NotImplementedError

    def is_dirt(self):
        return False