from __future__ import annotations

from .position import Position


class Point(Position):
    """
    A point is a location on the floor represented by two
    coordenates.

    Attributes:
        x (int): The x coordenate.
        y (int): The y coordenate.
    """

    def __init__(self, x: int, y: int) -> None:
        """
        Initializes a point.

        :param x: The x coordenate.
        :param y: The y coordenate.
        """
        self.x = x
        self.y = y

    def __eq__(self, other: Point) -> bool:
        """
        Verifies if the point is equal to another point.

        :param other: The other point to compare.
        :return: True if the points are equal, False otherwise.
        """
        return self.x == other.x and self.y == other.y
