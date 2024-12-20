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
# # Modularizing an Experiment with Functions
#
# The aim of this course is to learn how to create programs that are robust and reusable.
# Functions play an ingetral role in achieving this aim.
# Functions allow us to spearate our program into different logical units that have a clear scope and purpose.
# This allow us to reuse the same function in multiple programs.
# A function that does one thing can also be easily tested because its scope is limited. Finally, functions with a clear purpose and descriptive name make our code much more readable and act as a form of self-documenting code: it is very clear what unctions called `play_tone()` or `draw_circle()` do without having to consult any additional documentation.

# %%
# %pip install psychopy mypy
# %load_ext autoreload
# %autoreload 2

# %%
import random
from psychopy import prefs
prefs.hardware['audioLatencyMode'] = 0  # prevent psychtoolbox from taking over the sound card
from psychopy.sound import Sound
from psychopy.event import waitKeys
from psychopy.visual import Window
Sound(stereo=False);


# %% [markdown]
# ## 1. Defining Functions
#
# A function is defined by the `def` keyword, may accept certain input parameters and may `return` a result. A function has only access to the parameters that are passed to it as arguments and any result produced by the function can only be accessed by other parts of the program if that value is explicitly returned. This limited scope makes functions great for testing and robustness! In this notebook you will find many `assert` statements which test the functions that you will write. Don't worry about how exactly `assert` works just yet - just treat it as a tool that provides feedback on the correctness of your functions.
#
# ### Reference Table
# |Code | Duration |
# | ---| ---|
# |`def add(a,b):` <br> &nbsp;&nbsp;&nbsp;&nbsp; `return a+b` | Define an `add()` function that takes in two parameters `a` and `b` and returns their sum
# |`assert a == b` | Raise an `AssertionError` if `a` is NOT equal to `b`, otherwise do nothing |
# |`tone = Sound(value=350, secs=0.5)` | Create a `tone` at `350`Hz with a duration of `0.5` seconds |

# %% [markdown]
# **Example**: Write the `add()` function below, so that running the tests below shows `"Success!"`
#

# %%
def add(a,b):
    return a+b


# %%
assert add(2,3) == 5
assert add(4,4) == 8
print('Success!')

# %% [markdown]
# ---
# **Exercise**: Write the `subtract()` function below, so that running the tests below shows `"Success!"`

# %%

# %%
assert subtract(4,1) == 3
assert subtract(7,12) == -5
print('Success!')

# %%

# %%
assert is_odd(8) == False
assert is_odd(5) == True
print('Success!')

# %% [markdown]
# ---
# **Exercise**: Write the `make_list_of_zeros()` function below, so that running the tests below shows `"Success!"`
#

# %%

# %%
assert len(make_list_of_zeros(10)) == 10
for z in make_list_of_zeros(5):
    assert z == 0
print('Success!')

# %% [markdown]
# ---
# **Exercise**: Write a `fist_and_last()` function below, so that running the tests below shows "Success!". (Hint: to return multiple values, separate them by a comma: `return val1, val2`)

# %%

# %%
assert first_and_last([1,2,3,4]) == (1,4)
assert first_and_last(["x", "c"]) == ("x", "c")
print("Success!")

# %% [markdown]
# ---
# **Exercise**: Write the `make_tone()` function below, so that running the tests below shows `"Success!"`.<br>(Hint: `Sound(value==800).sound == 800`)
#

# %%

# %%
assert make_tone(500).sound == 500
assert make_tone(1200).sound == 1200
print('Success!')

# %% [markdown]
# ---
# **Exercise**: Write the `change_pitch()` function below, so that running the tests below shows `"Success!"`

# %%

# %%
tone = Sound(value=700)
assert change_pitch(tone, 50).sound == 750
assert change_pitch(tone, -100).sound == 600
print('Success!')

# %% [markdown]
# ----
# **Exercise**: Write the `cumulative_duration()` function below, so that running the tests below shows `"Success!"`

# %%

# %%
assert cumulative_duration(Sound(secs=1.2), Sound(secs=0.5)) == 1.7
assert cumulative_duration(Sound(secs=0.8), Sound(secs=2)) == 2.8


# %% [markdown]
# # 2. Optional Arguments
#
# Parameters be passed to a function based on their name or their position. For example, we can call the `say_hi_to()` function below as `say_hi_to("John", "Doe", True)`.
# However, this means we have to pass the parameters in the correct order.
# If we instead give the names of the parameters, we make the call more descriptive and independent of the parameters order: `say_hi_to(sout=True, first="John", last="Doe")`.
# Some arguments are **optional** which means that they have a default value defined in the function's definition.
# If we pass in a value for that parameter, the default will be overwritten, if not, the function will use the default.
#
#
# ### Reference Table
# |Code | Duration |
# | ---| ---|
# |`def add(a,b, c=0):` <br> &nbsp;&nbsp;&nbsp;&nbsp; `return a+b+c` | Define an `add()` function that takes in two required parameters `a` and `b` and an optional parameter `c` and returns their sum |
# |`key = waitKeys(keyList="space", timeStamped=True)` | Wait until the `"space"` key was pressed and return a list of lists with [[name, time]].|

# %% [markdown]
# **Example**: Write the `say_hi_to()` function below, so that running the tests below shows `"Success!"`

# %%
def say_hi_to(first, last="", shout=False):
    text = "Hi" + " " + first + " " + last + "!"
    if shout:
        return text.upper()
    else:
        return text


# %%
assert say_hi_to(first="Bob") == "Hi Bob !"
assert say_hi_to(first="Bob", last="McBobface") == "Hi Bob McBobface!"
assert say_hi_to(first="Bob", last="McBobface", shout=True) == "HI BOB MCBOBFACE!"
print("Success!")

# %% [markdown]
# ---
# **Exercise**: Write the `make_tone()` function below, so that running the tests below shows `"Success!"`

# %%

# %%
assert make_tone(550).sound == 550
assert make_tone(550).secs== 1.5
assert make_tone(750, 0.1).sound == 750
assert make_tone(750, 0.1).secs== 0.1
print("Success!")


# %% [markdown]
# ---
# **Exercise**: Write a `make_and_play_tone()` function below, so that running the tests below shows `"Success!"`

# %%

# %%
assert make_and_play_tone(500, duration=0.2, play=True).statusDetailed["State"] == 1
assert make_and_play_tone(500, 0.2).statusDetailed["State"] == 0
print("Success!")

# %% [markdown]
# ---
# **Exercise**: Write a `make_two_tones()` function below, so that running the tests below shows `"Success!"`

# %%

# %%
assert make_two_tones(250, 4000)[0].sound == 250
assert make_two_tones(250, 4000)[1].sound == 4000

# %% [markdown]
# ---
# **Exercise**: Write the `wait_keys()` function below, so that running the tests below shows `"Success!"`
#

# %%

# %%
with Window() as win:
    assert wait_keys(["space"]) == "space"
    assert len(wait_keys(timed=True)) == 2
print("Success!")
    

# %% [markdown]
# ---
# **Exercise**: Write a different `wait_keys()` function below, so that running the tests below shows `"Success!"`

# %%

# %%
with Window() as win:
    assert len(wait_keys()) == 2
    assert wait_keys()[0] == "space"

# %% [markdown]
# ## 3. Importing functions
#
# Importing allows us to make our code truly reusable. We can build up our own library of functions and import from this library across all of our projects.
# When we import functions we have to provide their full name, similar to how you would locate files and folders on your computer. For example, the function `add()` within the file `maths.py` can be imported as `from maths import add`. Just like with variables, there can every only be one function with the same name in your namespace, so if there already is a function called `add()`, it will be overwritten by this import.
# Alternatively, you could just `import maths` and call the function as `maths.add()`. This is a bit more to type but it will make sure that your other `add()` function is not overwritten.
#
# ### Reference Table
# |Code                      | Description                                         |
# |---                       | ---                                                 |
# |`import mymod` | Import the module `mymod`                                      |
# |`import mymod as m`       | Import the module `mymod` with the alias `m`     |
# |`from mymod import myfun` | Import the function `myfun` from the module `mymod` |
# |`from mymod import *`     | Import all functions from the module `mymod`        |
#

# %% [markdown]
# **Example**: Create a file `say_hi_to.py` that contains a `say_hi_to()` function, and import it so it passes the tests below

# %%
from say_hi_to import say_hi_to

# %%
assert say_hi_to(first="Bob") == "Hi Bob !"
assert say_hi_to(first="Bob", last="McBobface") == "Hi Bob McBobface!"
assert say_hi_to(first="Bob", last="McBobface", shout=True) == "HI BOB MCBOBFACE!"
print("Success!")

# %% [markdown]
# ---
# **Example**: Create a file `make_tone.py` that contains a `make_tone()` function and import it so it passes the tests below

# %%

# %%
assert make_tone(frequency=700).secs== 0.3
assert make_tone(duration=1).sound==300
print("Success!")


# %% [markdown]
# ---
# **Example**: Add a `make_and_play_tone()` function to `make_tone.py` and import it under the alias `mpt` so it passes the tests below

# %%

# %%
assert mpt(3000, duration=0.2, play=True).statusDetailed["State"] == 1
assert mpt(frequency=500, duration=0.2).statusDetailed["State"] == 0
print("Success!")

# %% [markdown]
# ---
# **Example**: Create a file `keys.py` that contains a `wait_three_keys()` function and import it passes the tests below

# %%

# %%
with Window() as win:
    assert keys.wait_three_keys("space", "space", "space") == ("space", "space", "space")
    assert keys.wait_three_keys("a", "b", "c") == ("a", "b", "c")
print("Success!")


# %% [markdown]
# ## 4. Type Hints
#
# Another great way of making code more readable is by introducing type hints. Type hints are an, entirely optional way of declaring the data type of the parameters and return values of a function. This allows specific type-checking tools to probe our code for logical inconsistencies. What's more, it gives additional information to the user by clearly declaring what types of data have to be provided as inputs and can be expected as returns. This can be really helpful to know, for example, if the length of a signal is defined in samples (an integer value) or in seconds (a float value).
#
# ### Reference Table
# |Code | Duration |
# | ---| ---|
# |`def say_hi(name:str):` <br> &nbsp;&nbsp;&nbsp;&nbsp; `return a/b` | Define a `say_hi()` function that takes in one string parameter `name` |
# |`def divide(a:int,b:int)->float:` <br> &nbsp;&nbsp;&nbsp;&nbsp; `return a/b` | Define a `divide()` function that takes in two integer parameters `a` and `b` and returns a float |
# |`!mypy my_module.py`  | Run MyPy to typecheck the functions in `my_module.py`
#

# %% [markdown]
# **Exercise** Add type hints to `find_primes` to indicate the types of the input and returned values

# %%
def find_primes(start, stop):
    primes=[]
    for i in range(start, stop):
        is_prime = True
        for j in range(2,int(i/2)):
            if i%j == 0:
                is_prime = False
        if is_prime:
            primes.append(i)
    return primes


# %%

# %% [markdown]
# ---
# **Exercise**: Add type hints to `say_hi_to()` to indictate the type of each variable and the type of the returned value

# %%
def shuffle_trials(trials, max_iter=1000) -> list:
    ok = False
    count = 0
    while not ok:
        count+=1
        if count > max_iter:
            raise StopIteration
        found_duplicate = False
        for i in range(1, len(trials)):
            if trials[i] == trials[i-1]:
                found_duplicate = True
        if not found_duplicate:
            ok = True
        else:
            random.shuffle(trials)
    return trials


# %%

# %% [markdown]
# ---
# **Exercise**: Add type hints to `say_hi_to()` to indictate the type of each variable and the type of the returned value

# %%
def say_hi_to(first, last="", do_print=False):
    text = "Hi" + " " + first + " " + last + "!"
    if print:
        print(text)
    else:
        return text

# %%

# %% [markdown]
# **Execise**: Move the type-annotated versions of `shuffle_trials()`, `find_primes()` and `say_hi_to()` to a new file called `my_functions.py`. Then run a static type analysis with MyPy using the script below

# %%
# !mypy ./my_module.py
