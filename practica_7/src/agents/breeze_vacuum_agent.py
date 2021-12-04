from __future__ import annotations
from typing import TYPE_CHECKING

from .vacuum_agent import VacuumAgent
from .sensors import BreezeSensor, DirtSensor, HoleSensor
from .actuators import BreezeActuator

if TYPE_CHECKING:
    from ..positions import Point
    from ..environments import Environment


class BreezeVacuumAgent(VacuumAgent):
    """
    A Vacuum Agent with memory. The memory is represented as a matrix.
    A negative value in the matrix means that point in the environment
    is free. Positive values indicate the level of danger of each point.
    The higher the value, the greater the danger.

    Attributes:
        _has_cleaned (bool): did the agent just clean the current
        position?

        _has_fallen (bool): did the agent just fell into a hole?
    """

    def __init__(self, position: Point) -> None:
        """
        Initialize an agent.

        :param position: The position of the agent.
        """
        super().__init__(
            position,
            sensors=[DirtSensor(self), BreezeSensor(self), HoleSensor(self)],
            actuators=[BreezeActuator(self)],
        )

        self.position: Point = position
        self.memory = [[0 for _ in range(16)] for _ in range(16)]

        self.memory[0][0] = -1

        self._has_cleaned: bool
        self._has_fallen: bool

    def add_peligrosity(self, env: Environment) -> None:
        """
        This method adds a level of danger in the agent's memory to the
        positions of possible holes.

        :param env: The environment in which the agent is acting.
        """

        self.memory[self.position.x][self.position.y] = -1

        for adj in env.adjacent_positions(self.position):
            if self.memory[adj.x][adj.y] != -1:
                self.memory[adj.x][adj.y] += 1

    def remove_peligrosity(self, env: Environment) -> None:
        """
        This method removes the danger marked in the agent's memory
        from the positions of possible holes.

        :param env: The environment in which the agent is acting.
        """

        self.memory[self.position.x][self.position.y] = -1
        for adj in env.adjacent_positions(self.position):
            self.memory[adj.x][adj.y] = -1

    def reward_performance(self) -> None:
        """
        Reward the agent for sensing something.
        """
        if self._has_cleaned:
            self.performance += 1
        elif self._has_fallen:
            self.performance -= 1000

    def punish_performance(self) -> None:
        """
        Punish the agent for not sensing anything.
        """
        if not self._has_cleaned:
            self.performance -= 1
