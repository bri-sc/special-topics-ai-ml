# Random Forests

One problem with decision trees that was highlighted previously is the risk of overfitting. 
A popular approach to address this is the use of a random forest. 
This combines many decision trees and aggregates the outputs of their classification. 

## How Do Random Forests Work?

````{margin}
```{note}
Bootstrap sampling is an important concept across statistics. 
```
````
A random forest consists of many individual decision trees, each trained on a different, random subset of the data. 
Giving each tree a different sample is known as *bootstrap* sampling. 
Instead of finding the best feature of all features to split each time, greater variance in the trees is achieved by randomly selecting a subset of features to split. 
This ensures that the trees explore different patterns in the data. 
Finally, to achieve the classification, each tree is used to predict the class, and then a majority vote is used to find the best possible class. 

```{figure} ../images/random-forests.png
---
name: random-forests
width: 60%
---
Three decision trees are being used to produce a random forest classification.
```

While a single decision tree can lead to overfitting. 
The averaging process of random forests reduces the risk of overfitting, even with very deep trees. 