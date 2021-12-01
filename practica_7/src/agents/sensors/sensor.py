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
        name (str): The name of the sensor.
    """

    def __init__(self, agent: Agent, name: str) -> None:
        """
        This method is used to initialize the sensor.

        :param agent: The agent that owns the sensor.
        :param name: The name of the sensor.
        """
        self.agent: Agent = agent
        self.name: str = name

    def sense(self, _: Environment) -> bool:
        """
        This method is used to sense the environment.

        :return: True if it senses something, False otherwise.
        """
        raise NotImplementedError
