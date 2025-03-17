# Generalised Adversarial Networks

Ian Goodfellow invented the generalised adversarial network, or GAN, a specific type of machine learning framework. 
The GAN consists of two competing neural networks: 
- the **generator** works to create synthetic data that is similar to the real data
- the **discriminator** identifies some data that comes from real data or the generator. 

The two networks compete, where the generator must create realistic data samples while the other tries to distinguish real samples from fake ones. 

The generator transforms some random noise vector into a data sample, such as an image. 
Many fake samples are mixed in with real samples, and the discriminator outputs a probability score indicating whether the sample is real or fake. 
Over time, the generator learns to improve the fakes it creates in an **adversarial game**. 

```{admonition} AI Art Generation
:class: tip
GANs became extremely popular with the birth of AI art generation tools such as Dall-E. 
While these are fun tools that can be used to create interesting art easily, they started an interesting discussion in the [media around copyright]. 
All artificial intelligences are *artificial*; an AI's work is based on the material that it has seen before and only that. 
The desire to use AI in the generation of art is seen by some as a good efficiency measure, allowing costs to be reduced. 
However, we should remember that art is most powerful when it tells us something new. 
Hence, the result of the recent Hollywood writer's strike would [not allow AI to replace writers](). 
```

To construct a GAN, we are combining many of the building blocks we have seen before, such as convolutional filters and loss functions. 
Therefore, let's push right ahead. 