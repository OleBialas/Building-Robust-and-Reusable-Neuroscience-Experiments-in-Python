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
# # VII. Automated Testing
#
# Manual testing is an integral part of software development. However, it does not scale well with the size of a project. The more your codebase grows the more time you have to spend testing. What's more, as things become more complex it becomes difficult to understanded all the interactions between different part of your code and it is easy to break one part of your program by modifying another one.
# This is where automated testing are invaluable. By building a suite of tests you can constantly verify that your code works as expected and that new features are being integrated properly!

# %%
# %pip install psychopy pytest ipytest pytest-cov

# %%
import random
import json
from psychopy.sound import Sound
from psychopy.visual import Window
from psychopy.event import waitKeys
import pytest
import ipytest
ipytest.autoconfig()
Sound(stereo=False);

# %% [markdown]
# ## 1. Writing Assert Statements
#
# A key component of every test is the `assert` statement. It tests that result of some part of the code is what you would expect. `assert` is really simple - it raises an `AssertionError` if whateber you are asserting evaluates to `False` and does nothing otherwise.
# Generally, more asserts are better but often it is a good idea to focus your test on interesting edge cases, like: what happens when you pass in an empty list to a function that accepts lists? What if a time parameter is zero or negative? And so on ...
#
# ### Reference Table
# |Code | Duration |
# | ---| ---|
# |`assert a == b` | Raise an `AssertionError` if `a` is NOT equal to `b`, otherwise do nothing |
# |`assert isinstance(a, int)` | Raise an `AssertionError` if `a` is not an integer, otherwise do nothing |
# |`assert a > b` | Raise an `AssertionError` if `a` is NOT greater than `b`, otherwise do nothing |
# |`tone = Sound(value=350, secs=0.5)` | Create a `tone` at `350`Hz with a duration of `0.5` seconds |
# |`key = waitKeys(keyList="space", timeStamped=True)` | Wait until the `"space"` key was pressed and return a list of lists with [[name, time]].|

# %% [markdown]
# **Example**: `assert` that the value `x` is positive and and `print("Success"!)`
#

# %%
x = random.random();

# %%
assert x>0
print("Success!")

# %% [markdown]
# **Exercise**: `assert` that the absolute difference between x and y is smaller than 1 and and `print("Success"!)`
#

# %%
x = random.random()
y = random.random();

# %%
# Solution
assert -1<(x-y)<1
assert abs(x-y)<1
print("Success!")

# %% [markdown]
# **Exercise**: `assert` that x is a string and `print("Success"!)`
#

# %%
x = "1";

# %%
# Solution
assert isinstance(x, str)
print("Success!")


# %% [markdown]
# **Exercise** Write two assert statements that check that:
# - the value returned by `subtract(3, 5)` is `-2`
# - the value returned by `subtract(10, 7)` is `3`
#
# and `print("Success"!)`

# %%
def subtract(a,b):
    return a-b


# %%
# Solution
assert subtract(3, 5) == -2
assert subtract(10,7) == 3
print("Success!")


# %% [markdown]
# **Exercise**: Write an `assert` statement that checks that:
# - the the length of the list returned by `concatenate_lists(a,b)` is equal to `len(a) + len(b)` 
#
# and `print("Success"!)`
#

# %%
def concatenate_lists(a,b):
    return a+b


# %%
# Solution
x1,x2 = [1,2,3], [2,3,4]
assert len(concatenate_lists(x1,x2)) == len(x1)+len(x2)
print("Success!")


# %% [markdown]
# **Exercise**: Write two `assert` statement that check that:
# - the tone returned by `make_tone(freq=800, dur=0.5)` has the attributes `tone.sound=800` and `tone.secs=0.5`
# - the tone returned by `make_tone(freq=1200, dur=0.3)` has the attributes `tone.sound=1200` and `tone.secs=0.3`
#
#
# and `print("Success"!)`

# %%
def make_tone(freq, dur):
    return Sound(value=freq, secs=dur)


# %%
# Solution
assert make_tone(freq=800, dur=0.5).sound == 800
assert make_tone(freq=800, dur=0.5).secs== 0.5
assert make_tone(freq=1200, dur=0.3).sound == 1200
assert make_tone(freq=1200, dur=0.3).secs== 0.3
print("Success!")


# %% [markdown]
# **Exercise**: Write four `assert` statement that check that:
# - The length of the list returned by `wait_keys(["space"])` is 1
# - The first element of the list returned by `wait_keys(["space"])` is `"space"`
# - The length of the list returned by `wait_keys(["space"], True)` is 2
# - The second element of the list returned by `wait_keys(["space"], True)` is a `float`
#
# and `print("Success"!)`
#
# Hint: you have to wrap you tests inside a Window context manager, like this: <br>
# `with Window() as win:` 
# <br> &nbsp;&nbsp;&nbsp;&nbsp; `assert ...`

# %%
def wait_keys(keys=None, timed=False):
    keys = waitKeys(keyList=keys, timeStamped=timed)
    if timed:
        return keys[0]
    else:
        return keys


# %%
# Solution
with Window() as win:
    assert len(wait_keys(["space"]))==1
    assert len(wait_keys(["space"], True))==2
    assert wait_keys(["space"])[0]=="space"
    assert isinstance(wait_keys(["space"], True)[1], float)


# %% [markdown]
# ## 2. Writing Test Functions
#
# Usually `assert` statments are not used on their own but wrapped inside test functions. Organizing your tests into functions provides the same advantages as organizing your code in functions: it makes them more readable, maintainable and robust. What's more, it allow tools such as Pytest to do the testing automatically and report to you any failed tests. In this section we are going to use Ipytest which is a convenient tool to use Pytest inside a Jupyter notebook: simply include an %%ipytest tag at the top of a cell and, when you execute it, Pytest will run every function in the cell that starts with `test_`. The rules for writing good test functions are the same as the rules for writing good function: each test should have a clear purpose an a name that reflects this purpose like `test_file_was_written()`.
#
# |Code | Description |
# | --- | ---         |
# |`%%ipytest` | Use Pytest to execute every function in a cell that starts with `test_` |
# | `with pytest.raises(ValueError):` <br> &nbsp;&nbsp;&nbsp;&nbsp; `divide(1, "hi)` | Assert that `divide(1,"hi")` raises a `ValueError`|

# %% [markdown]
# We are going to test the `trial_sequence()` function defined below

# %%
def trial_sequence(conditions: list, n_reps: int, shuffle:bool = True):
    trials = conditions * n_reps
    if shuffle:
        random.shuffle(trials)
    return trials



# %% [markdown]
# **Example**: Write a test function `test_trial_sequence_is_shuffled()` that tests that the returned list is shuffled when `shuffle=True`. Add the `%%ipytest` tag to the top of the cell and run it to execute that cell.

# %%
# %%ipytest
def test_trial_sequence_is_shuffled():
    trials1 = trial_sequence(conditions=[1,2,3], n_reps=1000)
    trials2 = trial_sequence(conditions=[1,2,3], n_reps=1000)
    assert trials1 != trials2


# %% [markdown]
# **Exercise**: Write a test function `test_trial_sequence_is_shuffled()` that tests that the returned list is ordered when `shuffle=True`. Add the `%%ipytest` tag to the top of the cell and run it to execute that cell.

# %%
# %%ipytest
# Solution
def test_trial_sequence_is_ordered():
    trials1 = trial_sequence(conditions=[1,2,3], n_reps=1000, shuffle=False)
    trials2 = trial_sequence(conditions=[1,2,3], n_reps=1000, shuffle=False)
    assert trials1 == trials2


# %% [markdown]
# **Exercise**: Write a test function that tests the list returned by `test_trial_sequence_is_shuffled()` has the correct `len()` using three different `assert` conditions . Add the `%%ipytest` tag to the top of the cell and run it to execute that cell.

# %%
# %%ipytest
# Solution
def test_trial_sequence_has_correct_len():
    trials = trial_sequence([1,2,3], n_reps=4)


# %% [markdown]
# ---
# We are going to test the `load_config` function defined in the cell below

# %%
def load_config(fpath:str):
    with open(fpath) as f:
        config = json.load(f)
    return config


# %% [markdown]
# **Exercise** Write a test function that tests that the dictionary returned by `load_config()` contains the keys `"conditions"` and `"n_trials"`.
#
#  (Hint: `"a" in config` is `True` if `config` contains a key named `"a"`)

# %%
# %%ipytest
# Solution
def test_config_has_keys():
    config = load_config("config.json")
    assert "conditions" in config
    assert "n_trials" in config


# %% [markdown]
# **Exercise** Write a test function that tests the value stored under the key "conditions" in the dictionary returned by `load_config()` is a list of integers

# %%
# %%ipytest
# Solution
def test_conditions_is_list_of_int():
    config = load_config("config.json")
    assert isinstance(config["conditions"], list)
    for c in config["conditions"]:
        assert isinstance(c, int)


# %% [markdown]
# **Exercise** Write a test function that tests that uses `pytest.raises` to test that `load_config` raises a `FileNotFoundError` when trying to load a file that does not exist

# %%
# %%ipytest
#Solution
def test_load_config_raises_error():
    with pytest.raises(FileNotFoundError):
        load_config("comfig.json")

# %% [markdown]
# ## 3. Runnig Pytest from the Terminal
#
# Now that we understand how Pytest works we can start to develop our test module. The tests work exactly the same as in a notebook but you put them in a separate file. Usually this file is named like the file it tests with the "test_" prefix (e.g. `test_my_module.py` would contain the tests for `my_module`.py). In the test module, you can import the functions you want to test and then test them.
# Organizing your test like this has the advantage that you can run all of them by simply calling pytest a single time.
# Per default, Pytest will open every Python file that starts with `test_` and, inside that file, run every function that starts with `test_`.
#
# This folder contains a function called `sequencegen.py` by that contains 3 functions:
# - `has_repetitions()` which checks if a trial seuquence has repetitions of the same element within the given `min_dist` and returns `True` or `False`
# - `make_sequene()` that creates a sequence from a list of `conditions` with a given number of `n_trials` and shuffles that list until `has_repetitions()` returns `False`
# - `write_sequence()` which writes the trials sequence to a file
#
# Let's test these functions!

# %% [markdown]
#
#
# **Exercise**: In this folder, create a new script called `test_sequencegen.py` where you `import` the three functions from `sequencegen.py`

# %% [markdown]
# **Exercise**: In this folder create a new function called `test_has_repetitions()` that tests that:
# - Calling `test_has_repetitions()` on a list that has a repetition returns `True`
# - Calling `test_has_repetitions()` on a list that has a repetition returns `False`
#
# Then execute the cell below to run Pytest

# %%
# !pytest

# %% [markdown]
# **Exercise**: add another function called `test_has_repetitions_respects_min_dist` to test that:
# - Calling `test_has_repetitions()` on a list that has a repetition further away that `min_dist` returns `False`
# - Calling `test_has_repetitions()` on a list that has a repetition within `min_dist` returns `True`
#
# Then execute the cell below to run Pytest

# %%
# !pytest

# %% [markdown]
# **Exercises**: Write a function called `test_sequence_has_correct_len()` that tests that the sequence returned by `make_sequence` has desired length given by `n_trials`.
#
# Then execute the cell below to run Pytest

# %%
# !pytest

# %% [markdown]
# **Exercises**: Write a function called `test_max_iterations()`, that uses `pytest.raises` to test that `make_sequence()` raises a `StopIteration` if you try to generate an impossible sequence (e.g. a sequence with a `min_dist` that is too large).
#
# Then execute the cell below to run Pytest

# %%
# !pytest

# %% [markdown]
# Another nice feature of pytest is that it can determine our test coverage which tells us the percentage of code that is covered by our tests.
# A test coverage below 100% means that there are certain parts of your code that are never executed.
# This can help us to identify any blind spots in our code. Just run the cell below to let Pytest mesure the test coverage for `sequencegen.py`

# %%
# !pytest --cov

# %% [markdown]
# ## 4. Parameterizing Tests
#
# Writing assert statements to tests all the different combinations of parameters that may be important for you program can be laborious. This is where parameterization is extremely useful. It provides us with an esy interface to run a large number of test. For example, we could test a function like `add` with a large number of values by parameterizing it with the `range()` function.
# Pytets will take all those values and run our test function with every single one.
# For this to work, the name in parameterize `"a"` must have the same name as the parameter of the test function `a`.
#
# ```python
# @pytest.mark.parametrize("a", range(1000))
# def test_add(a)
#     add(a+3) == a+3
# ```
#
# We can also parameterize multiple parameters. In this case, we pass in both variable names followed by a list of tuples, each of which contains the parameters for one run of the test. In the example below, `a` will take on the values 1, 3, and 4 and `b` will take on the values `2`, `4` and `6`.
#
# ```python
# @pytest.mark.parametrize("a, b", [(1,2), (3,4), (5,6)])
# def test_add(a, b):
#     assert add(a+b) == a+b 
# ```

# %% [markdown]
# **Exercise**: Parameterize the function `test_sequence_has_correct_len()` so that it tests that the sequence returned by `make_sequence` has desired length for  different values of `n_trials`

# %% [markdown]
# **Exercise**: Parameterize the function `test_max_iteration()` so that it tests that it raises a `StopIteration` if you try to generate a sequence with three different impossible combionations of `conditions` and `n_trials`.
