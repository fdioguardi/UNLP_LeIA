from __future__ import annotations
import random
from typing import TYPE_CHECKING

from .actuator import Actuator

if TYPE_CHECKING:
    from ...environments import Environment
    from ..breeze_vacuum_agent import BreezeVacuumAgent


class BreezeActuator(Actuator):
    """
    This class is used to represent an agent's actuator.

    This actuator moves the agent to a random adjacent position,
    indifferent of the presence of dirt in the environment.

    Attributes:
        agent (Agent): The agent to which this actuator belongs.
    """

    def __init__(self, agent: BreezeVacuumAgent):

        self.agent: BreezeVacuumAgent = agent

    def act(self, environment: Environment) -> None:
        """
        This method is used to perform the actuator's action.

        :param environment: The environment in which the actuator acts.
        """

        self.agent.move(
            random.choice(environment.adjacent_positions(self.agent.position))
        )

    def act_after_sensing(
        self, environment: Environment, sense_info: dict[str, bool]
    ) -> None:
        """
        This method is used to perform the actuator's action after
        having sensed dirt or breeze in the environment.

        :param environment: The environment in which the actuator acts.
        :param sense_info: The information collected by sensors.
        """

        if sense_info["Breeze sensor"]:
            self.mark_maybe_holes(environment)
            self.agent.breeze_positions.append(self.agent.position)

        else:
            self.unmark_maybe_holes(environment)
            self.agent.free_positions.append(self.agent.position)

    def mark_maybe_holes(self, environment: Environment):
        """
        This method fills the agent's memory with the positions of
        possible holes.

        :param environment: The environment in which the actuator acts.
        """
        self.agent.breeze_positions.append(self.agent.position)

        for pos in environment.adjacent_positions(self.agent.position):
            if not self.agent.is_known_position(pos):
                self.agent.maybe_hole_positions.append(pos)

    def unmark_maybe_holes(self, environment: Environment):
        """
        This method removes positions that were believed to be holes
        from the agent's memory.

        :param environment: The environment in which the actuator acts.
        """
        for pos in environment.adjacent_positions(self.agent.position):
            if pos in self.agent.maybe_hole_positions:
                self.agent.maybe_hole_positions.remove(pos)

    def act_after_not_sensing(
        self, environment: Environment, sense_info: dict[str, bool]
    ) -> None:
        """
        This method is used to perform the actuator's action after not
        sensing dirt or breeze in the environment.

        :param environment: The environment in which the actuator acts.
        :param sense_info: The information collected by sensors.
        """

        self.act(environment)
