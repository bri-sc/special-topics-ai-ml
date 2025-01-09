# Tools

## Jupyter Notebooks

````{margin}
```{note}
We use a tool called [Jupyter Book](https://jupyterbook.org/en/stable/intro.html) to convert the notebooks and markdown files to HTML, which is available online.
```
````
Jupyter Notebooks are a popular tool in the data science community. 
This is because they offer the ability to mix code and explanatory text. 
In fact, this entire course book is written as a series of Jupyter Notebooks and Markdown text files.
As with any tool, the Jupyter Notebook has some drawbacks; in fact, it is a popular subject for blogs: 
- [The Five Worst Things About Jupyter Notebooks](https://dev.to/chainguns/the-five-worst-things-about-jupyter-notebooks-5d4o)
- [When and how Jupyter Notebooks fail, and what to use instead](https://erikjandevries.medium.com/when-and-how-jupyter-notebooks-fail-and-what-to-use-instead-a52c27dbaa4c)
- [A Rant On Why I Despise Jupyter Notebooks](https://medium.com/codex/an-honest-rant-on-why-i-despise-jupyter-notebooks-6b631334ce19)
- [On the Myths and Problems of Jupyter Notebooks](https://ploomber.io/blog/nbs-myths/)

Personally, I ([Andrew McCluskey](https://mccluskey.scot)) like Notebooks as a place for preparing code and text to be descriptive of the work completed. 
For example, sharing some analysis with a colleague who is less comfortable with programming or prototyping a solution to a problem before building this into a large piece of code, such as a Python package.

```{admonition} Bristol Only
:class: bristol
In the SCIFM0002 unit, you are expected to be **comfortable** working with [Jupyter Notebooks](./jupyter-notebooks.ipynb). 
How you work with them is up to you: for example, you may want to install the Jupyter application or run your `.ipynb` files through [VSCode](https://code.visualstudio.com/docs/datascience/jupyter-notebooks). 
```

## Python Environments and Package Management

The Python ecosystem we will be using is vibrant; having so many packages with such a vast range of functionality can be extremely powerful. 
However, it comes with drawbacks, specifically around the compatibility of different packages. 
Therefore, the concept of Python environments has become popular. 
A Python environment is a sandbox containing a specific set of packages, aiming to ensure package compatibility and reproducibility of experience. 

````{margin}
```{note}
`mamba` is a reengineering of `conda` to improve speed. 
This was achieved by rewriting some of the dependency-checking algorithms in C++. 
```
````
There are a few different ways that we can work with Python environments. 
Python's *built-in* approach uses a tool called [`venv`](https://docs.python.org/3/library/venv.html). 
However, this is limited to using packages distributed through the Python Package Index (PyPI),i.e., with `pip`. 
A popular alternative is `conda` (or `mamba`). 
`conda` and `mamba` have the added functionality to be able to install [conda packages](https://anaconda.org/anaconda/repo) -- conda packages are more flexible than PyPI packages (it is easier to build a conda package with non-Python code included).

```{admonition} Conda Cheatsheet
:class: reading
It can, at times, be hard to remember all the different `conda` commands. 
Access to a [cheatsheet](https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf) can eb valuable in times like these.
```

To ensure that you have all of the necessary packages to work effectively with this course book, we provide the following environment file: [special-topics.yml](../_static/special-topics.yml). 
To install this environment, you should install [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) or [mamba](https://mamba.readthedocs.io/en/latest/installation/mamba-installation.html), and then create the environment by downloading the environment file and running the following command in the bash terminal:
```bash 
conda env create -f special-topics.yml
```
To activate this conda environment, the following command can be used:
```bash
conda activate special-topics
```
You should be able to access all the necessary packages to work through this course book from this environment. 

```{admonition} Bristol Only
:class: bristol
Similar to the Jupyter Notebooks, it is expected that you will be able to run within a conda environment. 
If you are running on Windows, installing this within the Windows Subsystem for Linux (WSL) partition is best.
You should work out how to run Jupyter Notebooks from the WSL partition to ensure you are accessing the relevant conda environment. 
If you have any trouble, speak to the unit director or one of the PhD student demonstrators.
```
