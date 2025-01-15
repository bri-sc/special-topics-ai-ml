# Clustering

Another unsupervised machine learning technique is clustering. 
The aim of clustering is to identify similarity between data points and, therefore, *cluster* them. 
This is a unsupervised approach, not requiring labels to be used.
Instead the positions of the data points in the feature space may provide a guide for the labels. 

```{figure} ../images/clustering.png
---
name: clustering
width: 66%
---
A visual representation of two different clusterings of the same dataset.
```

Clustering aims to find *natural* groupings in data. 
However, as a result it is dependent on the feature space in which the data is clustered.
Often some dimensionality reduction technique is used, prior to data clustering to provide a more meaningful *psuedo*-feature space.
But, many clustering alogrithms are capable of operating in *N*-dimensions, though our appreciation of them is limited to two or three. 

````{margin}
```{note}
Another mention for Carl Friedrich Gauss.
```
````
In this section, we will look at three popular and powerful clustering algorithms; *k*-means clustering, Gaussian mixture models and hierarchical clustering, but this is by no means the only approaches.
The `scikit-learn` documentation has a really nice [overview of clustering methods](https://scikit-learn.org/1.5/modules/clustering.html#overview-of-clustering-methods) that is great to look at.