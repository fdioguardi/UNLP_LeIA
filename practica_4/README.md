# :broom: Agente limpiador

Esta es una implementación en Python de un agente limpiador
que recoge tierra en un ambiente 2D.

## :nerd_face: Integrantes

- Felipe Dioguardi - 16211/4
- Leonardo Germán Loza Bonora - 16181/7
- Julian Marques de Abrantes - 15966/0

## :computer: Ejecución

El programa se ejecuta ingresando la siguiente línea en una consola
desde el directorio `practica_4`:

```bash
python main.py
```

## :open_file_folder: Estructura

El código fuente del repositorio se distribuye de la siguiente forma:

```file-tree
.
├── main.py
└── src
    ├── agents
    │   ├── actuators
    │   │   ├── actuator.py
    │   │   └── aspirator.py
    │   ├── agent.py
    │   ├── sensors
    │   │   ├── dirt_sensor.py
    │   │   └── sensor.py
    │   └── vacuum_agent.py
    ├── environments
    │   ├── environment.py
    │   └── xyenvironment.py
    ├── positions
    │   ├── point.py
    │   └── position.py
    └── things
        ├── dirt.py
        └── thing.py
```

### :dizzy: Elementos abstractos

- [`Agent`](./src/agents/agent.py): representa un agente genérico
  con un sensor y un actuador.

- [`Actuator`](./src/agents/actuators/actuator.py): representa un actuador genérico.

- [`Sensor`](./src/agents/sensors/sensor.py): representa un sensor genérico.

- [`Environment`](./src/environments/environment.py): representa un ambiente genérico
  con un agente y una lista de cosas que lo habitan.

- [`Position`](./src/positions/position.py): representa una posición de un ambiente.

- [`Thing`](./src/things/thing.py): representa una _cosa_ genérica.
  Cada _cosa_ será un habitante de algún ambiente.

### :sparkles: Elementos concretos

- [`VacuumAgent`](./src/agents/vacuum_agent.py): representa un agente limpiador.

- [`AspiratorActuator`](./src/agents/actuators/aspirator.py): representa al actuador
  de un agente limpiador.
  Se encarga de mover al agente de manera aleatoria y aspirar tierra en su posición.

- [`DirtSensor`](./src/agents/sensors/dirt_sensor.py): representa al sensor de
  tierra de un agente limpiador. Se encarga de detectar tierra
  en la posición del agente.

- [`XYEnvironment`](./src/environments/xyenvironment.py): representa un ambiente
  en 2 dimensiones (por ejemplo, un piso).

- [`Point`](./src/positions/point.py): representa una posición en un XYEnvironment.

- [`Dirt`](./src/things/dirt.py): representa tierra en un ambiente.
  Puede ser recogida por un agente como el VacuumAgent.

## :book: Fuentes

La idea de modelar los ambientes y agentes de esta forma surgió del
[repositorio de aima-python](https://github.com/aimacode/aima-python),
que contiene una [implementación propia](https://github.com/aimacode/aima-python/blob/668a2fb0bcd28b4963648c1425f904baa3826a8f/agents.py#L730)
del ejercicio.
