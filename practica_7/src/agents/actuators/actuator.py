from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...agents import Agent
    from ...environments import Environment


class Actuator:
    """
    This class is used to represent an agent's actuator.

    Attributes:
        agent (Agent): The agent that the actuator belongs to.
    """

    def __init__(self, agent: Agent) -> None:
        """
        This method is used to initialize the actuator.

        :param agent: The agent that the actuator belongs to.
        """
        self.agent: Agent = agent

    def act_after_sensing(self, _: Environment) -> None:
        """
        This method is used to act after sensing something with a
        sensor.

        :param _: The environment to act in.
        """
        raise NotImplementedError

    def act_after_not_sensing(self, _: Environment) -> None:
        """
        This method is used to act after not sensing anyting with a
        sensor.

        :param _: The environment to act in.
        """
        raise NotImplementedError
