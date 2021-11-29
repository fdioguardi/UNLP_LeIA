from __future__ import annotations
from typing import TYPE_CHECKING

from .actuators import AspiratorActuator
from .agent import Agent
from .sensors import DirtSensor

if TYPE_CHECKING:
    from ..positions import Position


class VacuumAgent(Agent):
    """
    An agent that simulates a vaccum cleaner picking dirt from the
    floor.

    Attributes:
        actuator (AspiratorActuator): The actuator that picks up dirt.
        sensor (DirtSensor): The sensor that detects dirt.
        performance (int): The performance of the agent.
        position (Position): The position of the agent.
    """

    def __init__(self, position: Position) -> None:
        """
        Initialize an agent.

        :param position: The position of the agent.
        """
        super().__init__(position, DirtSensor(self), AspiratorActuator(self))
        self.performance: int = 0

    def reward_performance(self) -> None:
        """
        Reward the agent for performing well.
        """
        self.performance += 1

    def punish_performance(self) -> None:
        """
        Punish the agent for performing poorly.
        """
        pass
