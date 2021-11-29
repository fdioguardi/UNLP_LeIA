from __future__ import annotations

from src.environments import XYEnvironment
from src.agents import VacuumAgent
from src.positions import Point
from src.things import Dirt, Hole


def main():
    agent = VacuumAgent(Point(0, 0))
    env = XYEnvironment(agent, 16, 16)

    # Add dirt to the environment
    for _ in range(env.width * env.height // 2):
        env.add_thing(Dirt(env.random_location_inbounds()))

    # Add holes to the environment
    for _ in range(4):
        env.add_thing(Hole(env.random_location_inbounds(), env))

    env.run()
    print(f"The agent's performance on this run was '{agent.performance}'.")


if __name__ == "__main__":
    main()
