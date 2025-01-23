# Dealing With Continuous Variables

Classification is the area of predicting discrete distributions, i.e., is a new data point a member of class `a` or `b`. 
However, there are a range of problems where it is desirable to predict a continuous variable. 
For example, a workflow to estimate a person's height based on features, such as their diet or the height of family members. 
Problems such as this are the domain of regression algorithms.

```{figure} ../images/regression.png
---
name: regression
width: 40%
---
The regression line describes a linear trend observed in *y*, given values of *x*.
```

Regression involves finding trends that can generally describe the observations based on features. 
Many machine learning workflows use linear regression, which is achieved through intelligent featurisation of the data. 
Here, we will look at polynomial regression and support vector regression in addition to linear regression methods. 