# Bayes Theorem

The natural progression from probabilistic modelling is to consider a Bayesian approach. 
The Bayesian paradigm of modelling is based on (1) the idea of probabilistic modelling in our understanding of the world, i.e., nothing is definite, and (2) including what we already understand about the world in our model. 
The probabilistic modelling handles the former, but the latter, the idea of prior knowledge, requires the use of Bayes' theorem. 

Bayes' theorem was first proposed by Rev. Thomas Bayes in 1763 {cite}`Bayes1763` and has the form, 

$$
p(A | B) = \frac{p(B | A) p(A)}{p(B)},
$$

where $p(A)$ is read as the probability of observing $A$ and $p(B | A)$ is the probability of observing $B$ given that $A$ has happened, the latter is known as a *conditional probability*.
We can think of Bayes' theorem as a tool for the inversion of conditional probabilities. 
Consider the example of the likelihood discussed previously, $p[D | M(\Theta)]$ is the probability of some data, $D$, being observed given some underlying model, $M$ with parameters, $\Theta$. 
Realistically, we aren't interested in the probability of observing some data; we are interested in the likelihood that our model describes some data we have observed, i.e., $p[M(\Theta) | D]$. 
Bayes' theorem can help us achieve this, and here we will look at how.

```{admonition} Further Reading 
:class: reading
There is a nice conceptual understanding of Bayes theorem in this 3Blue1Brown video.
<center>
<iframe width="560" height="315" src="https://www.youtube.com/embed/HZGCoVF3YvM?si=Hynn5XlF4l603sLR" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</center>
```