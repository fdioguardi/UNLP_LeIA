# :broom: Agente limpiador

Esta es una implementación en Python de un agente limpiador
que recoge tierra en un ambiente 2D con obstáculos.

## :nerd_face: Integrantes

- Felipe Dioguardi - 16211/4
- Leonardo Germán Loza Bonora - 16181/7
- Julian Marques de Abrantes - 15966/0

## :computer: Ejecución

El programa se ejecuta ingresando la siguiente línea en una consola
desde el directorio `practica_7`:

```bash
python main.py
```
Además se cuenta con un archivo de configuración 'config.ini' para
determinar si el agente conoce el nivel de suciedad del ambiente, la
cantidad de suciedad y la cantidad de agujeros.

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
    │   │   └── breeze_actuator.py
    │   ├── agent.py
    │   ├── sensors
    │   │   └── breeze_sensor.py
    │   │   ├── dirt_sensor.py
    │   │   └── hole_sensor.py
    │   │   └── sensor.py
    │   └── breeze_vacuum_agent.py
    │   └── vacuum_agent.py
    ├── environments
    │   ├── environment.py
    │   └── xyenvironment.py
    ├── positions
    │   ├── point.py
    │   └── position.py
    └── things
        ├── breeze.py
        ├── dirt.py
        ├── hole.py
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

- [`BreezeVacuumAgent`](./src/agents/breeze_vacuum_agent.py): representa un agente 
  limpiador con detector de brizas.

- [`BreezeActuator`](./src/agents/actuators/breeze_actuator.py): representa al actuador
  de un agente limpiador con detector de brizas.
  Se encarga de que el agente de aspire tierra en su posición, compruebe si no se ha
  caido en un agujero, compruebe si hay briza, calcule su próximo destino y se mueva.

- [`AspiratorActuator`](./src/agents/actuators/aspirator.py): representa al actuador
  de un agente limpiador.
  Se encarga de mover al agente de manera aleatoria y aspirar tierra en su posición.

- [`DirtSensor`](./src/agents/sensors/dirt_sensor.py): representa al sensor de
  tierra de un agente limpiador. Se encarga de detectar tierra
  en la posición del agente.

- [`BreezeSensor`](./src/agents/sensors/breeze_sensor.py): representa al sensor de
  brizas de un agente limpiador. Se encarga de detectar brizas
  en la posición del agente.

- [`HoleSensor`](./src/agents/sensors/hole_sensor.py): representa al sensor de
  agujeros de un agente limpiador. Se encarga de detectar agujeros
  en la posición del agente.

- [`XYEnvironment`](./src/environments/xyenvironment.py): representa un ambiente
  en 2 dimensiones (por ejemplo, un piso).

- [`Point`](./src/positions/point.py): representa una posición en un XYEnvironment.

- [`Dirt`](./src/things/dirt.py): representa tierra en un ambiente.
  Puede ser recogida por un agente como el VacuumAgent.

- [`Hole`](./src/things/hole.py): representa un hoyo en un ambiente por el que el
  agente no puede pasar.

- [`Breeze`](./src/things/breeze.py): representa briza formada en las posiciones
  adyacentes a los hoyos.

## :book: Fuentes

La idea de modelar los ambientes y agentes de esta forma surgió del
[repositorio de aima-python](https://github.com/aimacode/aima-python).
