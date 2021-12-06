from __future__ import annotations

from src.environments import XYEnvironment
from src.agents import BreezeVacuumAgent
from src.positions import Point
from src.things import Dirt, Hole


def main():
    agent = BreezeVacuumAgent(Point(0, 0), 4, True)
    env = XYEnvironment(agent, 4, 4)

    # Add dirt to the environment
    for _ in range(env.width * env.height // 2):
        dirt_location = env.random_location_inbounds()
        things = env.things_in_position(dirt_location)
        # chequea que no haya dirt en esa posicion
        if not any(isinstance(t, Dirt) for t in things):
            env.add_thing(Dirt(dirt_location))

    # Add holes to the environment
    for _ in range(2):
        location = env.random_location_inbounds()
        # evita el inicio
        while location.x == 0 and location.y == 0:
            location = env.random_location_inbounds()
        env.add_thing(Hole(location, env))

    env.run()
    print()
    print(f"The agent's performance on this run was '{agent.performance}'.")


if __name__ == "__main__":
    main()
