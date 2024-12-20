# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.6
#   kernelspec:
#     display_name: .venv
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Fixtures for Testing with Temporary Directories
#
# Handling files and directories is a common task in computational neuroscience, especially when working with data pipelines, experiment outputs, or simulation results. This lesson focuses on essential tools for managing files in Python and organizing automated tests for research projects. You'll start by learning pathlib.Path, a modern way to work with file paths in a clear, cross-platform manner. Next, you'll explore tempfile.TemporaryDirectory for creating temporary storage, ensuring experiments don’t clutter your file system. Building on this, you’ll discover how pytest's tmp_path streamlines temporary file management in automated tests. Finally, you’ll learn to create custom fixtures in pytest for setting up complex test environments, enabling more robust, reproducible, and scalable test designs. These tools will help you write cleaner code, avoid common file-handling pitfalls, and develop reliable, well-tested research software.

# %%
# %pip install pytest>=0.2.2 ipytest requests

# %%
from pathlib import Path
import pytest
import ipytest
import numpy as np
import pandas as pd
ipytest.autoconfig()

# %% [markdown]
# ### Dessecting File Paths into components using the PathLib package
#
# There's a lot of information in a file path; it's more than just a string!  For example, in the following path we might want to learn the following|
#
# `C|\\Users\Nick\Documents\Photos\greece.jpg`, `../Desktop/Photos`, and `/usr/nickdg/desktop/data/mouse.ome.tif`
#
#   - Whether the path is an **absolute** path on the filesystem or is **relative** to the current working directory,
#   - What drive the data is on
#   - What directory or directories the file is inside
#   - Whether a file or folder is listed
#   - What the file's name is 
#   - What the file's extension is
#   - Whether the file exists on our computer or not.
#    
# ... and so on.  If we want to extract this data, we could do some fancy coding to figure it out from the string itself, but there's no need--the built-in `pathlib.Path` type has a lot of helper methods to get this information.  Here, we'll try out some of the most commonly-used helper methods in order to read and write data, plus create files and folders, easily.
#
#
# |**Code** | **Description** |
# | :---  | :--- |
# | **`path = Path('path/to/file.txt')`** | Create a `Path` object |
# | **`path.name`** | Get the path's filename, without the directory | 
# | **`path.suffix`** | Get the path's file extension |
# | **`path.stem`** | Get the path's filename, without the file extension |
# | **`path.parent`** | Get the Parent Directory |
# | **`path.joinpath('newfile.txt')`** | Append a path to the end of the current path
# | **`path.exists()`** | Check whether this file exists on the current computer |
# | **`path.mkdir(exist_ok=True, parents=True)`** | Make a directory at this path. Don't raise an error if it already exists, or if the parents aren't yet created. |
# | **`text = path.read_text()`** | Read a text file. |
# | **`path.write_text(text)`** | Write text to a text file. |
#
#

# %%
from pathlib import Path

# %% [markdown]
# Execute the cell below to turn the string `"data/raw/iris.csv"` into a `Path` and answer the questions in the cells below

# %%
path = Path("data/raw/iris.csv")
path

# %% [markdown]
# **Exercise**: does the path described in `path` currently exist on the computer?

# %%

# %% [markdown]
# **Exercise**: What is the name of the file described in this filepath?

# %%

# %% [markdown]
# **Exercise**: What is the parent folder of the file described in this filepath?

# %%

# %% [markdown]
# **Exercise**: What is the file extension (e.g. the "suffix") of the file described in this filepath?

# %%

# %% [markdown]
# **Exercise**: What is the name of the file *without* the extension (e.g. the "stem") of the file described in this filepath?

# %%

# %% [markdown]
# **Exercise**: What is the parent directory the file described in this filepath?

# %%

# %% [markdown]
# **Exercise** Make a new path called "NewFolder", and call the `mkdir()` to create it on the computer.

# %%

# %% [markdown]
# **Exercise**: Make a text file: **hello.txt**, and write the text, 'Hi!' into the file.

# %%

# %% [markdown]
# **Exercise**: Confirm that the `hello.txt` file exists

# %%

# %% [markdown]
# **Exercise**: Read from your hello file to a string variable and display the contents

# %%

# %% [markdown]
# ### Working with Temporary Directories
#
# Sometimes, it is helpful to create a temporary directory to save files in, that you intend to delete later on in order to save space on the computer. However, keeping it cleaned up is not the most straightforward task.  This need is so common, that all operating systems (e.g. Windows, Mac OS, Linux) provide a special temporary directory that is self-cleaned-up whenever the operating system needs more space, making it so that you don't have to think about deleting the files!
#
# The built-in `TemporaryDirectory()` object from `tempfile` package in Python makes this simple to do; just follow the following receipe to get a fresh Path to a temporary directory on the computer, and save data to your heart's wish:
#
# | Code | Description |
# | :-- | :-- |
# | **`tmpdir = Path(TemporaryDirectory().name)`** | Creates a path to a potential temporary directory as a `Path` object. |
# | **`tmpdir.mkdir()`** |  Create the directory on disk. |
# | **`tmpfile = tmpdir.joinpath('file.txt')`** | Specifiy a filename in the temporary directory, making a temporary file. |
# | **`tmpfile.write_text('text')`** | Write text to the temporary file. |
#  

# %%
from tempfile import TemporaryDirectory
from pathlib import Path

# %% [markdown]
# **Exercises**: Create a temporary directory.  Where is it located on your computer?

# %%

# %% [markdown]
# **Exercise**: Create another temporary directory.  Where is it located now?

# %%

# %% [markdown]
# **Exercise**: Create a "hello.txt" file in a temporary directory.

# %%

# %% [markdown]
# ### Using the `tmp_path` fixture in PyTest to Automatically Create Temporary Directoroy Paths in Automated Tests
#
# In automated testing for neuroscience research, managing temporary files and directories is crucial to ensure that tests run in isolation without affecting real data. pytest's tmp_path fixture provides a convenient, built-in way to create temporary directories unique to each test. This prevents file conflicts and ensures a clean environment, making tests more reliable and reproducible. Researchers can use tmp_path to simulate file-based experiments, save intermediate results, or test data processing pipelines without manual cleanup. By leveraging this fixture, tests remain independent and maintainable, supporting robust software development practices in computational neuroscience.
#
#
# | Code | Description |
# | :-- | :-- |
# | **`def test_x(tmp_path):`** | Tells Pytest to create a temporary directory on disk, make it a `Path`, and pass it to the test function. |

# %% [markdown]
# **Exercises**

# %% [markdown]
# **Example**: Write the `data` variable to a json file, then read it back in.  Write a test to confirm that:
#   - The data that is read is identical to what was written.

# %%
# %%ipytest

import json

data = [1, 2, 3, 4, 5]

def test_can_read_back_written_data(tmp_path):
    
    path = tmp_path.joinpath('data.json')
    path.write_text(json.dumps(data))
    data2 = json.loads(path.read_text())
    assert data == data2
    
    

# %% [markdown]
# **Exercise**: Write the `message` variable to a text file, then read it back in.  Write a test to confirm that:
#   - The data that is read is identical to what was written.

# %%
message = "Hello, World!"


# %%

# %% [markdown]
# ### Using Test Fixtures in PyTest
#
#
# Writing fixtures in automated testing is essential for creating clear, maintainable, and reusable test setups. Fixtures define the initial conditions required for tests, such as creating mock datasets, initializing hardware interfaces, or setting up database connections. By centralizing setup code, fixtures reduce duplication, making tests cleaner and easier to understand. They also promote modular test design, allowing researchers to adapt tests as experimental conditions evolve. In neuroscience research, where data processing pipelines and computational models can be complex, using fixtures ensures that tests remain consistent, reproducible, and focused on specific functionality rather than setup details.
#
# This uses the "decorator" feature in Python (the "@" symbol before defining a function) pattern.  Below is an example:
#
# ```python
# @fixture
# def my_fixture():
#     return 3
#
# def test_fun(my_fixture):
#     assert my_fixture == 3
# ```

# %% [markdown]
# **Example**: Use the `dataset` test fixture below to write the following automated tests:
#   - None of the dataset's values are greater than 10  (Useful Functions: `np.max()`)
#   - None of the dataset's values are less than 0  (Useful Functions: `np.min()`)

# %%
@pytest.fixture
def dataset():
    return np.array([1, 5, 3, 6, 7, 7, 4, 2, 4, 5, 0, 1])



# %%
# %%ipytest

def test_data_max_is_less_than_10(dataset):
    assert np.max(dataset) <= 10

def test_data_is_not_negative(dataset):
    assert np.min(dataset) >= 0



# %% [markdown]
# **Exercise**: Fixtures can be used to reduce repetitive code; for example, to read in datasets.  Use the `titanic` test fixture below to write the following automated tests:
#   - All values in the 'age' column are positive (Useful Code: `data['age'].min()`)
#   - None of the values in the 'sex' column are missing (Useful Code: `data['sex'].isna().any()`)

# %%
@pytest.fixture(scope='module')
def titanic():
    return pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/refs/heads/master/raw/titanic.csv')


# %%

# %% [markdown]
# **Exercise**: Fixtures can be used in complex situations; for example, if you need to download a dataset in case you don't have it already on disk.  Use the `data_path` test fixture below to write any two of the following automated tests:
#   - The data path exists on your computer (Useful Code: `path.exists()`)
#   - The data path can be read by pandas without raising an error (Useful Code: `pd.read_csv(path)`)
#   - Once read by pandas, the data contains a column called "survived" (Useful Code: `'column_name' in data`)
#   - Once read by pandas, the data has more than 100 rows (Useful Code: `len(data) > 50`)

# %%
import os
from pathlib import Path    
import requests

@pytest.fixture()
def data_path() -> Path:
    if not os.path.exists('titanic.csv'):
        url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/refs/heads/master/raw/titanic.csv'
        r = requests.get(url)
        r.encoding = 'utf-8'
        text = r.text
        with open('titanic.csv', 'w') as f:
            f.write(text)
    
    return Path('titanic.csv')


# %%
