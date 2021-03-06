from __future__ import annotations
from typing import TYPE_CHECKING

from ...things import Dirt

from .sensor import Sensor

if TYPE_CHECKING:
    from ...environments import Environment
    from ..agent import Agent


class DirtSensor(Sensor):
    """
    This is a sensor that senses if there is dirt in the environment.

    Attributes:
        name (str): The name of the sensor.
        agent (Agent): The agent this sensor is attached to.
    """

    def __init__(self, agent: Agent):
        """
        This method is used to initialize the sensor.

        :param agent: The agent that owns the sensor.
        """
        super().__init__(agent, "Dirt sensor")

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
