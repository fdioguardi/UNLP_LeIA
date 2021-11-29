from __future__ import annotations
from typing import TYPE_CHECKING

from ...things import Dirt

from .sensor import Sensor

if TYPE_CHECKING:
    from ...environments import Environment


class DirtSensor(Sensor):
    """
    This is a sensor that senses if there is dirt in the environment.

    Attributes:
        agent (Agent): The agent this sensor is attached to.
    """

    def sense(self, environment: Environment) -> bool:
        """
        Sense the dirt in the environment.

        :param environment: The environment to sense the dirt in.
        :return: True if there is dirt in the environment, False
        otherwise.
        """

        dirt = environment.overlapping_with(self.agent)

        if not dirt:
            return False

        return isinstance(dirt[0], Dirt)
