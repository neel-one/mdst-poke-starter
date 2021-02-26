# mdst-poke-starter
Starter Files for Michigan Data Science Team Pokemon Bots Project

Make sure both node.js v10+ and python 3.6+ are installed.
If not already installed visit https://nodejs.org/en/ for node.js and https://www.python.org/downloads/ for python.

In terminal, install the python poke-env library
``` 
pip install poke-env 
```

In terminal, install a server to run your agent on a clone of https://pokemonshowdown.com
```
 git clone https://github.com/hsahovid/Pokemon-Showdown.git
```

In terminal, start your server by running
```
cd Pokemon-Showdown
node pokemon-showdown
```

## Creating your first Agent

All credit goes to the great documentation from https://poke-env.readthedocs.io

We will create an Agent that does not require training; as such we can inherit from `Player` class like this:

```
from poke_env.player.player import Player

class Agent(Player):
 ...
```

The Player base class requires that subclasses implement one function: `choose_move` which describes the action that your Agent will take given a battle state

`choose_move(self, battle: Battle) -> str` takes in a battle argument, provided to you by the poke-env infrastructure. The battle argument is an object that holds data about the state of the game as the current move. Dive into the documentation for specifics. It must return a string, specifically the move order encoded into a string.
The Battle object has multiple properties that can make it easy to access game state. 
In this example from the documentation, we can define our agent as such.

```
class Agent(Player):
 def move(self, battle):
  # If the player can attack, it will
  if battle.available_moves:
   # Finds the max base power move among available ones
   best_move = max(battle.available_moves, key = lambda move : move.base_power)
   # Serialize move into a move order string
   return self.create_order(best_move)
  else:
   # Make a random move otherwise
   return self.choose_random_move(battle)
```

In this case some of the methods and properties used were `battle.available_moves` and `move.base_power`. Poke-env's core objects, including Battle, Move, etc. provide many many attributes and methods that we can access data useful for creating Agents.

For a more detailed explanation, please visit the official documentation. This example is only meant to give a slight introduction to our environment for PokeRL.
