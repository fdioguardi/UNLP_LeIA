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
    A '1' in the memory means that the position is unknown.
    A '2' in the memory means that the position is safe.
    Any value smaller than 1 in the memory means that the position might
    be dangerous. The smaller the value, the more dangerous that
    position could be.

    Attributes:
        _has_cleaned (bool): did the agent just clean the current
        position?

        _has_fallen (bool): did the agent just fell into a hole?

        _known_dirt_level (bool): does the agent know the level of dirt
        in the enviroment.
    """

    def __init__(
        self, position: Point, dimension: int, known_dirt_level: bool
    ) -> None:
        """
        Initialize an agent.

        :param position: The position of the agent.
        :param dimension: The dimension of the memory matrix.
        :param known_dirt_level: does the agent know how much dirt the
        environment has?
        """
        super().__init__(
            position,
            sensors=[DirtSensor(self), BreezeSensor(self), HoleSensor(self)],
            actuators=[BreezeActuator(self)],
        )

        self.position: Point = position
        self.memory = [[1 for _ in range(dimension)] for _ in range(dimension)]

        self._has_cleaned: bool = False
        self._has_fallen: bool = False

        self._known_dirt_level: bool = known_dirt_level

    def add_dangerousness(self, env: Environment) -> None:
        """
        This method adds a level of danger in the agent's memory to the
        positions of possible holes.

        :param env: The environment in which the agent is acting.
        """

        if self.memory[self.position.x][self.position.y] == 2:
            return

        self.memory[self.position.x][self.position.y] = 2

        for adj in env.adjacent_positions(self.position):
            if self.memory[adj.x][adj.y] != 2:
                self.memory[adj.x][adj.y] -= 1

    def remove_dangerousness(self, env: Environment) -> None:
        """
        This method removes the danger marked in the agent's memory
        from the positions of possible holes.

        :param env: The environment in which the agent is acting.
        """
        if self.memory[self.position.x][self.position.y] == 2:
            return

        self.memory[self.position.x][self.position.y] = 2
        for adj in env.adjacent_positions(self.position):
            if self.memory[adj.x][adj.y] != 2:
                self.memory[adj.x][adj.y] = 1

    def reward_performance(self) -> None:
        """
        Reward the agent for sensing something.
        """
        if self._has_cleaned:
            self.performance += 5
        elif self._has_fallen:
            self.performance -= 1000

    def punish_performance(self) -> None:
        """
        Punish the agent for not sensing anything.
        """
        if not self._has_cleaned:
            self.performance -= 1

    def graphic_memory(self):
        for row in self.memory:
            print(row)

    def has_cleaned_all_dirt(self, env: Environment):
        if self._known_dirt_level:
            return not env.has_dirt()
        return False
