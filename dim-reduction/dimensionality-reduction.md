# What is Dimensionality Reduction?

Dimensionality reduction algorithms are a class of unsupervised machine learning algorithms. 
These algorithms aim to reduce the number of features in a dataset without losing too much important information. 

Humans are bad at visualising data in more than two dimensions. 
However, humans are very good at the identification of trends in data (some may say [too good](https://www.tylervigen.com/spurious-correlations)). 
Therefore, reducing the number of features in a given dataset can be desirable to facilitate visualisation. 
Often, this practice is followed by approaches such as trend identification (i.e., linear regression) or [clustering](/clustering/clustering.html). 

```{figure} ../images/dimensionality-reduction.png
---
name: dr
width: 100%
---
A visual representation of dimensionality reduction from three dimensions to one dimension.
```

There are many dimensionality reduction algorithms, but we will look in detail at just a couple, namely, principal components analysis (PCA) and t-distributed stochastic neighbour embedding (*t*-SNE). 