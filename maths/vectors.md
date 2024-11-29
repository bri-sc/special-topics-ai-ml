# Vectors

There are many ways to think about {term}`vectors`; in computing, a vector is a list of numbers, and in physics, a vector is a quantity with both magnitude and direction. 
The position of something (say a particle, an atom, or a rocket) in two-dimensional space can be described as a vector.
Three particles in space are shown in {numref}`particles`.
```{figure} ../images/particles.svg
---
name: particles
height: 300px
---
Particles in some arbitrary space.
```

These particles appear to be just *floating* in space, i.e., it is not possible to explain *where* they are. 
Typically, the positions of something is space are described with respect to some reference point, in this case, the origin position. 
The origin position is represented with the coordinates $(0, 0)$. 
```{figure} ../images/particles-origin.svg
---
name: particles-origin
height: 300px
---
The space is no longer arbitrary with the origin, $(0, 0)$, defined.
```

Vectors can then be used to describe the positions of the particles with respect to the origin. 
These vectors, shown in {numref}`particles-vectors` have a magnitude (the length of the arrow) and a direction (the way that the arrow is pointing). 
However, these properties of the vectors have no values yet. 
```{figure} ../images/particles-vectors.svg
---
name: particles-vectors
height: 300px
---
The vectors (yellow arrows) that describe the position of the particles with respect to the origin.
```

The values of these properties are defined with {term}`basis vectors`. 
Basis vectors describe the distances covered in the vector space where the particles exist. 
```{figure} ../images/particles-grid.svg
---
name: particles-grid
height: 300px
---
The basis vectors $\mathbf{i}$ and $\mathbf{j}$ shown. 
```

Using these basis vectors in {numref}`particles-grid`, it can be said that the vectors have the following values 

$$
\mathbf{r}_1 = 2\mathbf{i} + 4\mathbf{j}, \;\;\;\;\mathbf{r}_2 = 6\mathbf{i} + 3\mathbf{j}, \;\;\;\;\mathbf{r}_3 = 5\mathbf{i} + 1\mathbf{j}.
$$ (vectors-alt)

Alternatively, these can be written in mathematical matrix notation (as column vectors), where the top number is the number of steps in $\mathbf{i}$ and the bottom number is the number of steps in $\mathbf{j}$. 

$$
\mathbf{r}_1 = \begin{bmatrix} 2 \\ 4 \end{bmatrix}, \;\;\;\;\;\; \mathbf{r}_2 = \begin{bmatrix} 6 \\ 3 \end{bmatrix}, \;\;\;\;\;\; \mathbf{r}_3 = \begin{bmatrix} 5 \\ 1 \end{bmatrix}.
$$ (vectors)

````{margin}
```{note}
This may appear as an overly complex way to talk about cartesian space, but hopefully, the value of this will become clear moving forward.
```
````
```{figure} ../images/particles-arrows.svg
---
name: particles-arrows
height: 300px
---
The basis vectors outlining the particle vectors. 
```

Consider the notation in Eqn. {eq}`vectors`, where the vectors are described as vertical arrays of numbers. 
This way of thinking about vectors can help us when we want to use NumPy arrays to codify these. 

````{admonition} Task
:class: important
**Write**, using both notation styles shown above, values for the vectors $\mathbf{s}_1$, $\mathbf{s}_2$, and $\mathbf{s}_3$ that are shown in {numref}`particles-exercise`.

```{figure} ../images/particles-exercise.png
---
name: particles-exercise
height: 300px
---
A set of vectors that describe the new positions of particles in space.
```
````