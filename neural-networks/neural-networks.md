# Computers That Act Like Brains

Artificial neural networks are behind the recent boom in artificial intelligence. 
The technology behind tools like [ChatGPT](https://chatgpt.com) and [Midjourney](https://www.midjourney.com/home) are based on these artificial neural networks. 
The design of an artificial neural network is based on the concept of a neuron, the excitable cell that fires electric signals around our nervous systems. 

```{figure} ../images/artificial-neural-network.png
---
name: ann
height: 300px
---
A pictorial description of a fully connected artificial neural network with a single hidden layer and two outputs. 
```

````{margin}
```{note}
The concept of a **deep** neural network expects at least two hidden layers in the network. 
```
````
Like a nervous system, an artificial neural network consists of many individual artificial neurons.
These neurons are typically aggregated into layers, which perform different functions.
In our artificial neural network, the signals travel from the input layers to the output layers.
They may pass through one or more intermediate hidden layers on this journey.
These hidden layers are defined as either taking inputs or providing outputs.

This section will start with the basics of how an artificial neuron works, building up understanding to reach convolutional and recurrent networks. 
This will give us the understanding to use these important tools and extrapolate them to investigate more complex networks in the future. 