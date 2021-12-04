from __future__ import annotations
from typing import TYPE_CHECKING

from ...things import Hole

from .sensor import Sensor

if TYPE_CHECKING:
    from ...environments import Environment
    from ..agent import Agent


class HoleSensor(Sensor):
    """
    This is a sensor that senses if there is a hole in the environment.

    Attributes:
        name (str): The name of the sensor.
        agent (Agent): The agent this sensor is attached to.
    """

    def __init__(self, agent: Agent):
        """
        This method is used to initialize the sensor.

        :param agent: The agent that owns the sensor.
        """
        super().__init__(agent, "Hole sensor")

    def sense(self, environment: Environment) -> bool:
        """
        Sense a hole in the environment.

        :param environment: The environment to sense the a hole in.
        :return: True if there is breeze in the environment, False
        otherwise.
        """
        things = environment.overlapping_with(self.agent)
        return any(isinstance(thing, Hole) for thing in things)
