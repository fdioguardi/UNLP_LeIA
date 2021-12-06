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
        self.visited_positions = []
        self.posible_positions = []

    def search(self, environment, position):
        if (position in self.visited_positions):
            return
        self.visited_positions.append(position)
        
        # si hay un bloqueo, vuelve
        if (self.agent.memory[position.x][position.y] < 1):
            return
        # si es una posicion sin descubrir, la agrega a posible
        elif (self.agent.memory[position.x][position.y] == 1):
            self.posible_positions.append(position)
            return
        else:
            for pos in environment.adjacent_positions(position):
                self.search(environment, pos)

    def search_position(self, environment):
        self.visited_positions = []
        self.posible_positions = []
        self.search(environment, self.agent.position)

    def move(self, environment: Environment) -> None:
        """
        This method is used to perform the actuator's movement.

        :param environment: The environment in which the actuator moves.
        """

        #print("Posicion actual: " + str(self.agent.position.x) + "," + str(self.agent.position.y))
        self.search_position(environment)
        if (len(self.posible_positions)):
            # se puede mover para algun lado
            self.agent.move(self.posible_positions[0])
            pass
        else:
            # no se puede mover más porque está bloqueado
            # decidimos si terminar el algoritmo acá
            # o si elegir un lugar peligroso para moverse
            # con posibilidad de caer en un hoyo
            self.agent.end()
            pass
        #print("Proxima posicion: " + str(self.agent.position.x) + "," + str(self.agent.position.y))
        """
        self.agent.move(
            min(
                environment.adjacent_positions(self.agent.position),
                key=lambda a: self.agent.memory[a.x][a.y],
            )
        )
        """

    def act_after_sensing(
        self, environment: Environment, sense_info: dict[str, bool]
    ) -> None:
        """
        This method is used to perform the actuator's action after
        having sensed dirt, breeze, or a hole in the environment.

        :param environment: The environment in which the actuator acts.
        :param sense_info: The information collected by sensors.
        """

        
        if sense_info["Hole sensor"]:
            print("-> Hole detected")
            self.agent._has_fallen = True
            self.agent.end()
        elif sense_info["Breeze sensor"]:
            print("-> Breeze detected")
            self.agent.add_peligrosity(environment)
        else:
            self.agent.remove_peligrosity(environment)

        self.agent._has_cleaned = environment.clean_dirt_in_position(self.agent.position)
        if (self.agent._has_cleaned) :
            print("-> Dirt cleaned")

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
