from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...environments import Environment
    from ...agents import Agent


class Sensor:
    """
    This class is used to represent an agent's sensor.

    Attributes:
        agent (Agent): The agent that owns the sensor.
    """

    def __init__(self, agent: Agent) -> None:
        """
        This method is used to initialize the sensor.

        :param agent: The agent that owns the sensor.
        """
        self.agent: Agent = agent

    def sense(self, _: Environment):
        """
        This method is used to sense the environment.
        """
        raise NotImplementedError
