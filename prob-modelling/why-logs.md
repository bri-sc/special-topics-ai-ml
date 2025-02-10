# Why Does Bayesian Modelling Use Logs?

You may notice in a lot of Bayesian modelling applications, the use of logarithmic values. 
For example, you may see that the log-likelihood is the parameter that is optimised, instead of the likelihood. 
Or similar for the log-posterior, over the posterior. 

The reason for this is simple, probabilities can be very small and therefore the logarithm of the probability is often more computational effective. 
By this, we mean that by computing the probability and not the logarithm, we my encounter numerical issues, from very very small floating point numbers. 
The reason we must be congnisent of this is that it may lead to a change in how we compute Bayes' theorem, i.e., 

````{margin}
```{note}
This is simply the application of rules of logarithms. 
```
````
$$
\ln[p(A | B)] = \ln\left[\frac{p(B | A) p(A)}{p(B)}\right] = \ln[p(B | A)] + \ln[p(A)] - \ln[p(B)]. 
$$

A popular Markov chain Monte Carlo sampling Python package, called [`emcee`](https://emcee.readthedocs.io/en/stable/) includes a tutorial here the negative log-likelihood is used to find the starting point for the MCMC algorithm, for exactly this reason. 