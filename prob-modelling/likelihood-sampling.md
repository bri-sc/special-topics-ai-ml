# Likelihood Sampling

In the previous section, we were looking at finding the maximum likelihood for some data given a model with parameters. 
However, the broad aim of looking at probabilistic modelling is to give us tools to understand those parameters. 
The data have uncertainty associated with them, therefore, the parameters of the model should have the same. 
While, it is possible to develop estimates of these parametric uncertainty from optimisation routines, a more rigorous approach is sampling.

In many ways, to compute the uncertainties, we want to sample the *unknown* probability distribution that describes the parameters of the model. 
While, this may sound trivial, for probability distributions over many dimensions--the number of dimensions is the number of parameter--can become very computationally intensive.
Therefore, a variety of algorithms have been developed to address this, here we will look at Markov chain Monte Carlo sampling, which is one of the most popular approach to likelihood sampling.
The result of both of these sampling algorithm is a set of values for the parameters, and a histogram of these will provide an estimate of the probability distributions.