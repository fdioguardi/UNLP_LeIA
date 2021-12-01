from __future__ import annotations
from typing import TYPE_CHECKING

from .vacuum_agent import VacuumAgent
from .sensors import BreezeSensor, DirtSensor
from .actuators import BreezeActuator

if TYPE_CHECKING:
    from ..positions import Position


class BreezeVacuumAgent(VacuumAgent):
    def __init__(self, position: Position) -> None:
        """
        Initialize an agent.

        :param position: The position of the agent.
        """
        super().__init__(
            position,
            sensors=[DirtSensor(self), BreezeSensor(self)],
            actuators=[BreezeActuator(self)],
        )

        # Memory
        self.breeze_positions = []
        self.free_positions = [self.position]
        self.hole_positions = []
        self.maybe_hole_positions = []

    def is_known_position(self, pos: Position) -> bool:
        return pos in (
            self.breeze_positions
            + self.free_positions
            + self.hole_positions
            + self.maybe_hole_positions
        )
