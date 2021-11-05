from __future__ import annotations
import random
from typing import TYPE_CHECKING

from .actuator import Actuator

if TYPE_CHECKING:
    from src.environments import Environment


class AspiratorActuator(Actuator):
    """
    This class is used to represent an agent's actuator.

    This actuator moves the agent to a random adjacent position,
    indifferent of the presence of dirt in the environment.

    Attributes:
        agent (Agent): The agent to which this actuator belongs.
    """

    def act(self, environment: Environment) -> None:
        """
        This method is used to perform the actuator's action.

        :param environment: The environment in which the actuator acts.
        """

        self.agent.move(
            random.choice(environment.adjacent_positions(self.agent.position))
        )

    def act_after_sensing(self, environment: Environment) -> None:
        """
        This method is used to perform the actuator's action after
        having sensed dirt in the environment.

        :param environment: The environment in which the actuator acts.
        """

        self.act(environment)

    def act_after_not_sensing(self, environment: Environment) -> None:
        """
        This method is used to perform the actuator's action after not
        sensing dirt in the environment.

        :param environment: The environment in which the actuator acts.
        """

        self.act(environment)
