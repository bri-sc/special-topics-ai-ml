# Classifiers 

Classifiers are a supervised machine learning approach that aims to predict discrete labels or categories for an object. 
A typical example of a classification problem is in image recognition, i.e., deciding if an image contains a picture of a cat or a dog. 
Strictly speaking, classification is a general approach in machine learning, but in this section, we will look at *statistical* classification approaches: logistic regression, decision trees and support vector machines. 
We can think of classification as being a supervised machine learning approach for predicting samples from discrete probability distributions, while [regression](/regression/regression) is used for continuous distributions. 

```{figure} ../images/classification.png
---
name: classification
width: 40%
---
The aim of a classification algorithm is to find the model (solid black line) or basis vectors *x* and *y* that discriminate blue and yellow as best as possible. 
```

```{admonition} A Cautionary Tale
:class: warning
A popular cautionary tale in machine learning is that of a classification algorithm that was used to determine if an image contained either a dog or a wolf. 
This algorithm was very successful when applied to the curated datasets defined by the researcher. 
However, after investigating the areas of *interest* in images that the classified was paying attention to. 
It was discovered that the only thing the classifier was interested in when deciding if an image had a dog or a wolf was how much snow was in the background. 
The data we train our algorithms on is as important, if not more so, than the approaches we use. 
```