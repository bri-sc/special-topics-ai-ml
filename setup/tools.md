# Tools

## Jupyter Notebooks

````{margin}
```{note}
We use a tool called [Jupyter Book](https://jupyterbook.org/en/stable/intro.html) to convert the notebooks and markdown files to html that is available online.
```
````
Jupyter Notebooks are a popular tool in the data science community. 
This is because they offer the ability to mix code and explanitory text. 
In fact, this entire course book is written as a series of Jupyter Notebooks (LINK TO GITHUB REPO) and Markdown text files.
As with any tool, the Jupyter Notebook has some drawbacks, in fact it is a popuylar subject for blogs: 
- [The Five Worst Things About Jupyter Notebooks](https://dev.to/chainguns/the-five-worst-things-about-jupyter-notebooks-5d4o)
- [When and how Jupyter Notebooks fail, and what to use instead](https://erikjandevries.medium.com/when-and-how-jupyter-notebooks-fail-and-what-to-use-instead-a52c27dbaa4c)
- [A Rant On Why I Despise Jupyter Notebooks](https://medium.com/codex/an-honest-rant-on-why-i-despise-jupyter-notebooks-6b631334ce19)
- [On the Myths and Problems of Jupyter Notebooks](https://ploomber.io/blog/nbs-myths/)

Personally, I ([Andrew McCluskey](https://mccluskey.scot)) like Notebooks, as a place for preparing code and text to be descriptive of the work completed. 
For example, sharing some analysis with a colleague that is less comfortable with programming or prototyping a solution to a problem before building this into a large piece of code, such as a Python package.

```{admonition} Bristol Only
:class: bristol
In the SCIFM0002 unit, it is expected that you will are **comfortable** working with [Jupyter Notebooks](./jupyter-notebooks.ipynb). 
How you work with them is up to you: for example, you may want to install the Jupyter application or run your `.ipynb` files through [VSCode](https://code.visualstudio.com/docs/datascience/jupyter-notebooks). 
```

## Python Environments and Package Management

The Python ecosystem taht we will be using is extremely rich, having so many packages with such a vast range of functionality can be extremely powerful. 
However, it comes with drawbacks, specifically around compatibility of different packages. 
Therefore, the concept of Python environments has become popular. 
A Python enviroment is a sandbox that contains a specific set of packages, with the aim of ensuring package compatibility and reproducibility of experience. 

````{margin}
```{note}
`mamba` is a reengineering of `conda` to improve speed. 
This was achieved by rewriting some of the dependency checking algorithms in C++. 
```
````
There are a few different ways that we can work with Python enviroments. 
The *built-in* approach in Python is to use a tool called [`venv`](https://docs.python.org/3/library/venv.html). 
However, this is limited to using packages that are distributed through the Python Package Index (PyPI),i.e., with `pip`. 
A popular alternative is `conda` (or `mamba`). 
`conda` and `mamba` have the added functionality to be able to install [conda packages](https://anaconda.org/anaconda/repo) -- conda packages are more flexible than PyPI packages (it is easier to build a conda package with non-Python code included).

To ensure that you have all of the necessary packages to work effectively with this course book, we provide the following environment file: [special-topics.yml](../_static/special-topics.yml). 
To install this environment, you should install [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) or [mamba](https://mamba.readthedocs.io/en/latest/installation/mamba-installation.html), and then create the environment by downloading the environment file and running the following command in the bash terminal:
```bash 
conda env create -f special-topics.yml
```
To activate this conda enviroment, the following command can be used:
```bash
conda activate special-topics
```
From this environment, you should be able to access all of the necessary pacakges to work through this course book. 

```{admonition} Bristol Only
:class: bristol
Similar to the Jupyter Notebooks, it is expected that you will be able to run within a conda environment. 
If you are running on Windows, it is best to install this within the Windows Subsystem for Linux (WSL) partition.
You should work out how to run Jupyter Notebooks from the WSL partition to ensure you are accessing the relevant conda environment. 
If you have any trouble, speak to the unit director or one of the PhD student demonstrators.
```
