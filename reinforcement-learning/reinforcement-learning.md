# Learning From Our Mistakes

````{margin}
```{note}
The founder of DeepMind, Demis Hassabis, was awarded the Nobel Prize in Chemistry for the later development of the AlphaFold model.
```
````
Reinforcement learning concepts have existed since the 1950s, resulting in various interesting uses. 
An example you may be familiar with is the Roomba vacuum system, which uses a reinforcement learning algorithm to find the most efficient way to vacuum a space. 
Probably the most well-known example of reinforcement learning is from 2016/2017, when a British start-up company called DeepMind developed an artificial intelligence by reinforcement learning that was capable of beating world champion [Go](https://en.wikipedia.org/wiki/Go_(game)) players. 

The AlphaGo model was built using a neural network, but the approach to training this network differs from previously investigated. 
Reinforcement learning does not involve training weights and parameters against known data and assessing it with tests. 
Instead, a software *agent* makes *observations* and then takes *action* within an *environment*; in return, the agent receives some *reward*.
The aim of the reinforcement learning algorithm is to optimise the expected reward over time, producing the best actions based on *policies*. 

```{figure} ./../images/reinforcement-learning.png
---
height: 300px
align: center
---
A diagram of the reinforcement learning loop.
```

## Learning to Optimise Rewards

Let's think about a few examples of the reward optimisation loop that reinforcement learning may harness: 
- In the example above of the Roomba-style robot vacuum, the actions are the movements the robot makes around the space (the environment), and the rewards would be the time taken to cover the complete space. 
- An agent may be some video game, in which case the environment is a simulation of the game, the actions are the inputs on the controller, and rewards are points scored in the game. 
- A smart home thermostat may be an agent, where rewards are given whenever it is close to a target temperature or saves energy; negative rewards would be then the human needs to intervene to adapt to the temperature. 

Rewards don't need to be positive; they can also be negative. 