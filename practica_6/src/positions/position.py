from __future__ import annotations


class Position:
    """
    A position on the floor.
    """

    def __eq__(self, _: Position) -> bool:
        """
        Verifies if the position is equal to another position.

        :param _: The position to compare to.
        :return: True if the positions are equal, False otherwise.
        """
        raise NotImplementedError
