# Distributions

Probability distributions are mathematical objects that we use to describe our data. 
It describes how the probability of outcomes is spread over the possible values of the data. 
Generally, any data we measure will follow some potentially unknown probability distribution. 
The probability distributions we use to describe some data must represent the data and the underlying physics and chemistry. 

Probability distributions can be either discrete or continuous. 
This language is probably familiar from the discussion of Fourier transforms. 
But to reiterate, a discrete distribution deals with countable objects with discrete (usually integer) values, like flipping a coin or rolling a dice. 
A continuous distribution handles things that can have any values (i.e., floating point numbers); these are more commonly found in scientific applications. 

## Properties of Probability Distributions

All probability distributions have a series of properties associated with them. 
These describe information about the distribution and, therefore, the data that the distribution describes: 
- Parameters: probability distributions are mathematical functions with variable parameters. These parameters control the shape and location of the distribution. 
- Expected value (mean) and variance: most distributions have properties of the average value of the distribution and the spread of values that it can range over. 
- Probability Mass/Density Function: the probability mass function (PMF) describes the probability of each outcome for a discrete distribution. While the probability density function (PDF) describes the probability that a given distribution will have a given value. 
- Cumulative Distribution Function (CDF): describes the probability that a random variable will be less than some value in the distribution. 

You may become familiar with many other properties of probability distributions in due course. 
However, let's look at discrete and continuous distributions individually. 

## Discrete Distributions

````{margin}
```{note}
Wikipedia is an excellent resource for properties of specific probability distributions. 
```
````
The most common discrete probability distribution people are introduced to is the [Bernoulli distribution](https://en.wikipedia.org/wiki/Bernoulli_distribution).
This distribution is associated with a typical example of the probability of flipping a coin and is a special case of a more general [binomial distribution](https://en.wikipedia.org/wiki/Binomial_distribution).
A random variable sampled from a Bernoulli distribution will take a value of 1 (we could call this heads) with a probability of $p$ and a value of 0 (i.e., tails) with a probability of $q = 1- p$. 
A "fair" coin would have a value of $p$ of 0.5, and heads and tails would be equally likely.

An important discrete distribution in scientific applications is the [Poisson distribution](https://en.wikipedia.org/wiki/Poisson_distribution). 
This describes the probability of a given number of *events* occurring in a fixed time interval. 
The PMF of a Poisson distribution has the following formula, 

$$
P(k) = \frac{\lambda^ke^{-\lambda}}{k!},
$$ 

where $\lambda$ is the parameter of the distribution.
The Poisson distribution has an important application in scientific observations, where there is a given number of observations in a time period. 
Consider a [photon-counting detector](https://en.wikipedia.org/wiki/Photon_counting), which is commonly used across the physical and biological sciences.
Each photon that interacts with the detector in a given time period is another "event", and therefore, the Poisson distribution can be used to describe the distribution of the photons and estimate uncertainty in the detector observations. 

```{figure} https://upload.wikimedia.org/wikipedia/commons/1/16/Poisson_pmf.svg
---
name: poisson
height: 300px
---
A plot of the Poisson distribution for three different values of the $\lambda$ parameter. Sourced from [Wikipedia](https://en.wikipedia.org/wiki/Poisson_distribution#/media/File:Poisson_pmf.svg) under a Creative Commons licence. 
```

## Continuous Distributions

````{margin}
```{note}
The normal distribution is also known as a Gaussian distribution, after [Carl Friedrich Gauss](https://en.wikipedia.org/wiki/Carl_Friedrich_Gauss), the second time he has been mentioned.
```
````
The most important continuous distribution is the [normal distribution](https://en.wikipedia.org/wiki/Normal_distribution). 
The importance of this distribution comes from its role as the result of the **central limit theorem**. 
```{admonition} Central Limit Theorem
:class: tip 
The central limit theorem states that the average of many observations of a random variable is itself a random variable -- whose distribution converges to a normal distribution. 
```
Therefore, the normal distribution is commonly used to describe physical measurements. 
In fact, when you see error bars on a plot, these usually describe a normal distribution's variance. 

The normal distribution has two parameters: the mean, $\mu$, and the variance, $\sigma^2$.
From these parameters, the normal distribution has the probability density function, 

$$
P(x) = \frac{1}{\sqrt{2\pi\sigma^2}}\exp{\left[-\dfrac{(x - \mu)^2}{2\sigma^2}\right]}.
$$

You may see the following notation used to describe a normal distribution, $\mathcal{N}(\mu, \sigma^2)$, such that a random variable from a normal distribution is $X \sim \mathcal{N}(\mu, \sigma^2)$.

The final distribution to highlight before moving on to practical matters is the [uniform distribution](https://en.wikipedia.org/wiki/Continuous_uniform_distribution). 
A random variable from a uniform distribution is equally likely to be any value between the bounds $a$ and $b$, i.e., $X \sim \mathcal{U}[a, b]$. 
The probability of obtaining a variable outwith those bounds is 0. 
So, the PDF is 

$$
P(x) = \begin{cases} 
    \dfrac{1}{b-a} & \text{for } x \in [a, b] \\
    &\\  % blank row
    0 & \text{otherwise}.
\end{cases}
$$

As we will see, the uniform distribution is vital in Bayesian optimisation problems, where the input parameters to some models must be bounded such that they cannot take unphysical values. 


