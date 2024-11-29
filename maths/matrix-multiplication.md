# Matrix Multiplication

Matrix multiplication may not be familiar to everyone therefore, we will discuss it using the concept of algorithmic thinking to break down the complexity. 
Note, that we can use NumPy to perform matrix multiplication but it is valuable to know what the process is. 
However, you may want to think of this page as a reference, as it can be easy to forgot the algorithm. 

Consider the requirement to multiply two matrices, for example;

```{math}
:label: matrices1
\mathbf{A} = \begin{bmatrix}
 4 & 1 \\ 5 & 3 \\ 1 & 2 \\ 2 & 2
 \end{bmatrix}
\;\;\;\;\;\;\;\;\;
\mathbf{B} = \begin{bmatrix}
 2 & 1 & 3 \\ 2 & 5 & 1
 \end{bmatrix}.
```

However, the algorithm should be general, therefore the matrices can be written in general terms 

```{math}
:label: matrices2
\mathbf{A} = \begin{bmatrix}
 a_{11} & a_{12} \\ a_{21} & a_{22} \\ a_{31} & a_{32} \\ a_{41} & a_{42}
 \end{bmatrix}
\;\;\;\;\;\;\;\;\;
\mathbf{B} = \begin{bmatrix}
 b_{11} & b_{12} & b_{13} \\ b_{21} & b_{22} & b_{23}
 \end{bmatrix},
```
where the symbols in Eqn. {eq}`matrices2` may be swapped for the numbers in Eqn. {eq}`matrices1` (or any other matrix). 

The leading matrix, $\mathbf{A}$, has the shape 4 &times; 2 and the trailing, $\mathbf{B}$, has the shape 2 &times; 3. 
The number of columns in the first matrix must be equal to the number of rows in the second and therefore, these matrices can be multiplied.

The resulting matrix, $\mathbf{C}$, will have the shape: number of rows in the leading matrix &times; number of columns in the trailing matrix. 
Therefore, $\mathbf{C}$ will have the shape 4 &times; 3, which can be written generally as 

```{math}
:label: matrix_c
\mathbf{C} = \begin{bmatrix}
 c_{11} & c_{12} & c_{13} \\ c_{21} & c_{22} & c_{23} \\ c_{31} & c_{32} & c_{33} \\ c_{41} & c_{42} & c_{43}
\end{bmatrix}
```

Then starting with $c_{11}$, this is calculated as the sum of the pairwise product of the matching row in $\mathbf{A}$ and the matching column in $\mathbf{B}$, i.e., $c_{11} = a_{11} b_{11} + a_{12} b_{21}$.
Next $c_{12}$ and $c_{13}$ are found with the same process. 

Once we reach the end of the row, the next row is computed $c_{21}$, $c_{22}$, etc. and this process continues until all of the values in $\mathbf{C}$ have been filled. 
This process is shown graphically below.

```{figure} https://upload.wikimedia.org/wikipedia/commons/thumb/e/eb/Matrix_multiplication_diagram_2.svg/1280px-Matrix_multiplication_diagram_2.svg.png
---
height: 300 px
---
A schematic diagram of matrix multiplication. Source: [Wikipedia/Matrix multiplication](https://commons.wikimedia.org/wiki/File:Matrix_multiplication_diagram.svg)
```

## Algorithm

Above, the process of matrix multiplication is described in full and hopefully, it is possible to follow the logic. 
However, this prose-heavy description would not be effective for a computer, which operates [very literally](https://www.youtube.com/watch?v=Ct-lOOUqmyY). 
Therefore, the algorithm must be described in such a way that it may be translated into computer code. 

```{mermaid}
flowchart TB;
 a{{Is the number of columns in \n<b>A</b> is the same as number of rows in <b>B</b>?}};
 b[\Cannot multiply these matrices/];
 c(Generate empty matrix, <b>C</b> with the shape, number of rows in <b>A</b> by number of columns in <b>B</b>);
 d(<i>i = 1</i> and <i>j = 1</i>);
 e{{Pairwise multiply row <i>i</i> in \n<b>A</b> by column <i>j</i> in <b>B</b> and store the array in the variable <i>x</i>}};
 f(Sum the values in <i>x</i>);
 g(Place result in <b>C</b> position <i>ij</i>);
 h{{Is <i>j</i> equal to the number of columns in <b>B</b>?}};
 i(Increase <i>i</i> by 1 and make <i>j=1</i>);
 j(Increase <i>j</i> by 1);
 k{{Is <i>i</i> equal to the number of rows in <b>A</b>?}};
 l[\Matrix multiplication complete/];
 a-->|No|b;
 a-->|Yes|c;
 c-->d;
 d-->e;
 e-->f;
 f-->g;
 g-->h;
 h-->|Yes|k;
 i-->e;
 h-->|No|j;
 j-->e;
 k-->|No|i;
 k-->|Yes|l;
```
<figcaption align="center" id="diagram">
 <p>
 <span class="caption-number">Diagram 2. </span>
 <span class="caption-text">
 An algorithm for matrix multiplication between leading matrix <span class="math notranslate nohighlight">\(\mathbf{A}\)</span> and trailing matrix <span class="math notranslate nohighlight">\(\mathbf{B}\)</span>.
 </span>
 <a class="headerlink" href="#diagram" title="Permalink to this diagram">#</a>
 </p>
</figcaption>