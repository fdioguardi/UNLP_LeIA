from __future__ import annotations

from src.environments import XYEnvironment
from src.agents import BreezeVacuumAgent
from src.positions import Point
from src.things import Dirt, Hole

import configparser

def main():
    config = configparser.ConfigParser()
    
    try:
        config.read("config.ini")
        agent_knows_dirt = (config['params']['agent_knows_dirt'] == 'True')
    except:
        agent_knows_dirt = False

    agent = BreezeVacuumAgent(Point(0, 0), 4, agent_knows_dirt)
    env = XYEnvironment(agent, 4, 4)

    # Add dirt to the environment
    try:
        amount_of_dirt = int(config['params']['amount_of_dirt'])
    except:
        amount_of_dirt = env.width * env.height // 2

    for _ in range(amount_of_dirt):
        dirt_location = env.random_location_inbounds()
        things = env.things_in_position(dirt_location)

        # chequea que no haya dirt en esa posicion
        if not any(isinstance(t, Dirt) for t in things):
            env.add_thing(Dirt(dirt_location))

    # Add holes to the environment
    try:
        amount_of_holes = int(config['params']['amount_of_holes'])
    except:
        amount_of_holes = 2
    
    for _ in range(amount_of_holes):
        location = env.random_location_inbounds()

        # evita el inicio
        while location.x == 0 and location.y == 0:
            location = env.random_location_inbounds()

        env.add_thing(Hole(location, env))

    env.run()
    print(f"\nThe agent's performance on this run was '{agent.performance}'.")


if __name__ == "__main__":
    main()
