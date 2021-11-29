from __future__ import annotations
from typing import TYPE_CHECKING

from ..things import Thing

if TYPE_CHECKING:
    from .actuators import Actuator
    from .sensors import Sensor
    from ..environments import Environment
    from ..positions import Position


class Agent(Thing):
    """
    An agent is a thing that can move around an environment.

    Attributes:
        actuator (Actuator): The actuator of the agent.
        performance (int): The performance of the agent.
        position (Position): The position of the agent.
        sensor (Sensor): The sensor of the agent.
    """

    def __init__(
        self, position: Position, sensor: Sensor, actuator: Actuator
    ) -> None:
        """
        Initialize an agent.

        :param position: The position of the agent.
        :param sensor: The sensor of the agent.
        :param actuator: The actuator of the agent.
        """
        super().__init__(position)
        self.performance: int = 0
        self.sensor: Sensor = sensor
        self.actuator: Actuator = actuator

    def move(self, position: Position) -> None:
        """
        Move the agent to the given position.

        :param position: The position to move to.
        """
        self.position = position

    def act(self, environment: Environment) -> None:
        """
        Perform one step in the environment.

        :param environment: The environment to act in.
        """

        if self.sensor.sense(environment):
            self.actuator.act_after_sensing(environment)
            self.reward_performance()
        else:
            self.actuator.act_after_not_sensing(environment)
            self.punish_performance()

    def reward_performance(self) -> None:
        """
        Reward the agent for performing well.
        """
        raise NotImplementedError

    def punish_performance(self) -> None:
        """
        Punish the agent for performing poorly.
        """
        raise NotImplementedError
