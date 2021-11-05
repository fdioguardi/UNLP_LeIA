from __future__ import annotations

from src.environments import XYEnvironment
from src.agents import VacuumAgent
from src.positions import Point
from src.things import Dirt


def main():
    agent = VacuumAgent(Point(0, 1))
    env = XYEnvironment(agent, 10, 10)

    for _ in range(env.width * env.height // 2):
        env.add_thing(Dirt(env.random_location_inbounds()))

    env.run()
    print(agent.performance)


if __name__ == "__main__":
    main()
