from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from src.agents import Agent
    from src.positions import Position
    from src.things import Thing


class Environment:
    """
    An environment represents a physical place where things can be
    placed.

    Attributes:
        agent (Agent): The agent in the environment.
        things (list[Thing]): A list of things in the environment.
    """

    def __init__(self, agent: Agent) -> None:
        self.things: list = []
        self.agent: Agent = agent

    def run(self, steps: int = 100) -> bool:
        """
        Run the Environment for given number of time steps or until
        the agent is done.

        :param steps: number of time steps to run the environment.
        :return: True if the environment is done, False otherwise.
        """
        for _ in range(steps):
            if self.is_done():
                return True
            self.step()

        return self.is_done()

    def step(self) -> None:
        """
        Perform one step in the environment.
        """
        if not self.is_done():
            self.agent.act(self)

    def is_done(self) -> bool:
        """
        Check if the environment is done.

        :return: True if there are no things remaining in the
        environment, False otherwise.
        """
        return self.things == []

    def adjacent_positions(self, _: Position) -> list:
        """
        Returns a list of positions adjacent to the given position.

        :return: A list of positions adjacent to the given position.
        """
        raise NotImplementedError

    def overlaps(self, thing: Thing) -> bool:
        """
        Check if the given thing overlaps with any other thing in
        the environment.

        :param thing: The thing to check for overlaps.
        :return: True if there is an overlap, False otherwise.
        """
        return any(thing.overlaps(t) for t in self.things)

    def overlapping_with(self, thing: Thing) -> list:
        """
        Returns a list of things overlapping with the given thing.

        :param thing: The thing to check for overlaps.
        :return: A list of things overlapping with the given thing.
        """
        return [t for t in self.things if t.overlaps(thing)]

    def clear(self, position: Position) -> bool:
        """
        Remove the thing at the given position.

        :param position: The position to clear.
        :return: True if the thing was removed, False otherwise.
        """
        for thing in self.things:
            if thing.position == position:
                self.things.remove(thing)
                return True

        return False
