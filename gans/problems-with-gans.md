# Mode Collapse in Training GANs

We highlighted that GANs can be technically challenging to train. 
One of the most common and complex to recognise/address is *mode collapse*. 
Mode collapse occurs when the generator produces a limited or repetitive set of outputs. 
Typically, this is because this subset can consistently fool the discriminator, but it leads to poor overall performance. 
An example of mode collapse in the [MNIST digits](../setup/datasets.ipynb) dataset would be if the generator only produces values of 3 and 8 instead of all 10 digits. 

We might call mode collapse in the optimisation context, getting stuck in a local minima. 
This is where the optimisation of some problem finds a local minima instead of the global minima. 
We address traditional optimisation problems by using more computationally intensive global optimisation strategies. 
However, with the huge number of parameters in a neural network problem, it is impossible to use these. 

Mode collapse can be either partial or complete. 
Partial mode collapse is where the generator collapses onto a subset of outcomes, while complete is where the same output is returned every time. 

## How To Address Mode Collapse?

There are a variety of strategies to address mode collapse. 
These include: 

1. Adding noise to the real data. 
    By adding random noise that changes with each iteration, it may be possible to mitigate some of the mode collapse factors. 
2. Using a different loss function. 
    Special loss functions, such as those implemented in the [Wasserstein GAN-GP](https://github.com/Lornatang/WassersteinGAN_GP-PyTorch), can help reduce the risk of mode collapse. 
3.  Use *feature matching*. 
    Instead of playing the adversarial game on the images themselves, train on some feature of the image, i.e., a two-dimensional Fourier transform. 
4. Unroll the GAN. 
    This is where the discriminator and the generator are updated unevenly. 
    So, for example, the discriminator is updated twice for every generator update. 
5. Optimisation of hyperparameters. 
    Hopefully, the previous section has made it clear that there are a variety of hyperparameters in the GAN training process. 
    Sometimes, mode collapse can be addressed simply by changing these. 
