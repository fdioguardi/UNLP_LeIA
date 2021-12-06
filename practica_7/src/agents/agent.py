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
        actuators (list[Actuator]): The actuators of the agent.
        performance (int): The performance of the agent.
        position (Position): The position of the agent.
        sensors (list[Sensor]): The sensors of the agent.
    """

    def __init__(
        self,
        position: Position,
        sensors: list[Sensor],
        actuators: list[Actuator],
    ) -> None:
        """
        Initialize an agent.

        :param position: The position of the agent.
        :param sensors: A list with the sensors of the agent.
        :param actuators: A list with the actuators of the agent.
        """
        super().__init__(position)
        self.performance: int = 0
        self.sensors: list[Sensor] = sensors
        self.actuators: list[Actuator] = actuators
        self.is_done = False

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

        sense_info = {
            sensor.name: sensor.sense(environment) for sensor in self.sensors
        }

        if any(sense_info.values()):
            for actuator in self.actuators:
                actuator.act_after_sensing(environment, sense_info)
            self.reward_performance()
        else:
            for actuator in self.actuators:
                actuator.act_after_not_sensing(environment, sense_info)
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

    def end(self):
        """
        Set an ending to the agent's journey.
        """
        self.is_done = True

    def graphic_memory(self):
        """
        Outputs a representation of the agent's memory to stdout.
        """
        print("No memory")

