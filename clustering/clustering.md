# Clustering

Another unsupervised machine learning technique is clustering. 
Clustering aims to identify similarities between data points and, therefore, *cluster* them. 
This is an unsupervised approach, not requiring labels to be used.
Instead, the positions of the data points in the feature space may provide a guide for the labels. 

```{figure} ../images/clustering.png
---
name: clustering
width: 66%
---
A visual representation of two different clusterings of the same dataset.
```

Clustering aims to find *natural* groupings in data. 
However, as a result, it depends on the feature space in which the data is clustered.
Some dimensionality reduction techniques are often used before data clustering to provide a more meaningful *psuedo*-feature space.
But, many clustering algorithms can operate in *N*-dimensions, though our appreciation of them is limited to two or three. 

````{margin}
```{note}
Another mention of Carl Friedrich Gauss.
```
````
In this section, we will look at three popular and powerful clustering algorithms: *k*-means clustering, Gaussian mixture models and hierarchical clustering, but this is by no means the only approach.
The `scikit-learn` documentation has a nice [overview of clustering methods](https://scikit-learn.org/1.5/modules/clustering.html#overview-of-clustering-methods) that is great to look at.