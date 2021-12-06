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
        self.posible_path = []

    def _find(self, environment, position):
        if (position in self.visited_positions):
            return
        self.visited_positions.append(position)
        
        # si hay un bloqueo, vuelve
        if (self.agent.memory[position.x][position.y] < 1):
            return
        # si es una posicion sin descubrir, la guarda
        elif (self.agent.memory[position.x][position.y] == 1):
            self.posible_path.append(position)
            return
        else:
            # busca en las posiciones adyacentes solo
            # si no encontro la posicion sin descubrir
            for pos in environment.adjacent_positions(position):
                if not self.has_path():
                    self._find(environment, pos)
            if self.has_path():
                self.posible_path.append(position)

    def find_new_path(self, environment):
        self.visited_positions = []
        self.posible_path = []
        self._find(environment, self.agent.position)

        # remueve la posicion actual
        if (self.has_path()):
            self.posible_path.pop()

    def has_path(self):
        return (len(self.posible_path) > 0)

    def next_path_position(self):
        return self.posible_path.pop()

    def move(self, environment: Environment) -> None:
        """
        This method is used to perform the actuator's movement.

        :param environment: The environment in which the actuator moves.
        """
        # si hay un camino posible determinado, lo sigue
        if (self.has_path()):
            self.agent.move(self.next_path_position())
            return

        self.find_new_path(environment)
        if (self.has_path()):
            # se puede mover para algun lado
            self.agent.move(self.next_path_position())
        else:
            # no se puede mover más porque está bloqueado
            # se puede implementar movimiento con probabilidad de caida
            self.agent.end()

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

        if (self.agent.has_cleaned_all_dirt(environment)):
            self.agent.end()
        elif not self.agent._has_fallen:
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
