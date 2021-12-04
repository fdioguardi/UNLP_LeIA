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

    def move(self, environment: Environment) -> None:
        """
        This method is used to perform the actuator's movement.

        :param environment: The environment in which the actuator moves.
        """

        self.agent.move(
            min(
                environment.adjacent_positions(self.agent.position),
                key=lambda a: self.agent.memory[a.x][a.y],
            )
        )

    def act_after_sensing(
        self, environment: Environment, sense_info: dict[str, bool]
    ) -> None:
        """
        This method is used to perform the actuator's action after
        having sensed dirt, breeze, or a hole in the environment.

        :param environment: The environment in which the actuator acts.
        :param sense_info: The information collected by sensors.
        """

        if sense_info["Breeze sensor"]:
            self.agent.add_peligrosity(environment)
        elif sense_info["Hole sensor"]:
            self.agent._has_fallen = True
        else:
            self.agent._has_cleaned = environment.clear(self.agent.position)
            self.agent.remove_peligrosity(environment)

        if not self.agent._has_fallen:
            self.move(environment)

    def act_after_not_sensing(
        self, environment: Environment, _: dict[str, bool]
    ) -> None:
        """
        This method is used to perform the actuator's action after not
        sensing dirt, holes, nor breeze in the environment.

        :param environment: The environment in which the actuator acts.
        :param _: The information collected by sensors.
        """

        self.agent.remove_peligrosity(environment)
        self.agent._has_cleaned = False
        self.agent._has_fallen = False

        self.move(environment)
