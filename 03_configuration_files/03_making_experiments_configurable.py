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
# # Configuring an Experiment
#
# Designing an experiment involves making lots of different choices, for example: What different conditions are being tested? What stimuli are presented? How many trials does the experiment contain?
# Often, as we pilot our studies or run additional control experiments, we want to change some aspect of our experiment.
# If all these parameters are directly stored in the code, we have to modify our program for every little change.
# Thus, it is convenient to store our parameters in a configuration file and load this file into our program.
# This way, we can run endless variations of our experiment without ever touching the code - this makes our program much more resuable!

# %%
# %pip install psychopy

# %%
import json
from psychopy.event import waitKeys
from psychopy.visual import Rect, Circle, TextStim, Window

# %% [markdown]
# ## 1. File Handling
#
# To store and load data, we have to interact with files.
# Python's builtin `open()` function allows to do exactly that: it returns a file object that we can use to read from and write to a specific file.
# The `open()` function is usually used within a context manager that is declared using the keyword `with`.
# This context manager makes our code more readable and also makes sure that our file is closed after we are done.
#
# ### Reference Table
# |Code | Description |
# |---  | ---|
# |`f = open("novel.txt", "w")` | `open` the file `"novel.txt"` in `"w"` (writing) mode |
# |`f = write("Once upon a time ...")` | Write to the opened file |
# | `f.close()`  | Close the file again |
# | `f = open("novel.txt", "r")` | `open` the file `"novel.txt"` in "r" (reading) mode |
# | `text = f.read()` | Read the opened file |
# | `with open("novel.txt", "w") as f:` <br> &nbsp;&nbsp;&nbsp;&nbsp; `f.write("...and they lived happily ever after.")` | Write to a file within a context manager that opens and automatically closes the file again. |

# %% [markdown]
# **Exercise**: `open` the file `"paper.txt"` in `"w"` mode, `write` the string `"Introduction"` to that file and `close` it again. Then, open the file in your editor.

# %%

# %% [markdown]
# Now, open `"paper.txt"` in `"r"` mode and `read` the file's content

# %%

# %% [markdown]
# ---
# **Exercise**: `open` a file called `"data.txt"` in `"w"` mode, `write` the string `"1,2,3,4,5,6"` to that file and `close` it again:

# %%

# %% [markdown]
# Open `"data.txt"` in your editor and, on a new line, add thee numbers **7,8,9,10,11,12** and save. Then open `"data.txt"` in `"r"` mode and `read` the file's content

# %%

# %% [markdown]
# ---
# **Exercise**: `open` the file `"conditions.txt"` in `"w"` mode `with` a context manager write the string `"a,b,c"` to that file:

# %%

# %% [markdown]
# Open `"conditions.txt"` in your text editor and manually add the letter **d** to the sequence of conditions. Then, open the file in `"r"` mode `with` a context manager and read the file and print its content
#

# %%

# %% [markdown]
# ---
# **Exercise**: `open` the file `"trials.txt"` in `"w"` mode `with` a context manager. Use a `for` loop within that contex to convert each element in `trials` to a string and write it on a new line in the file. (Hint: the string `"\n"` represents a line break)

# %%
trials = [1, 2, 3, 4, 5];

# %%

# %% [markdown]
# Open `"trials.txt"` in "r" mode `with` a context manager, `read` it and print its content

# %%

# %% [markdown]
# ## 2. Reading and Writing Configuration Files
#
# To work with configuration files, we need a data structure to represent them in Python.
# We are going to use dictionaries, which store data as a combination of keys and values.
# This is useful because we can give informative names to our parameters and make our code easier to read.
# When we save these dictionaries to our computer we are going to use the JSON format (this stands for JavaScript Object Notation).
# JSON has a syntax that is highly similar to Python dictionaries, so they can easily be converted to one another.
# Also, JSON files can be opened in any text editor, so we can edit them by hand which is very convenient!
#
# |Code | Description |
# |---|---|
# |`x = {"n": 100, "p": 0.5}`| Define a dictionary `x` with the keys `"n"` and `"p"` and the values `100` and `0.5`|
# | `with open("p.json", "w") as f:` <br> &nbsp;&nbsp;&nbsp;&nbsp; `json.dump(x, f)` | Write the dictionary `x` to the file `"p.json"`|
# | `with open("p.json", "w") as f:` <br> &nbsp;&nbsp;&nbsp;&nbsp; `json.dump(x, f, indent=3)` | Write the dictionary `x` to the file `"p.json"` and `indent` each level with `3` spaces|
# | `with open("p.json", "w") as f:` <br> &nbsp;&nbsp;&nbsp;&nbsp; `x = json.load(f)` | Load the file `"p.json"` and store its content in the dictionary `x`|

# %% [markdown]
# **Exercise**: Create a dictionary with `"n_trials": 100` and `"training": true"` and `"feedback": None` and write it to a file called `"parameters.json"`:

# %%

# %% [markdown]
# Open `"parameters.json"` in your editor --- how are the values `True` and `None` represented? Load the file's contents into a dictionary called `p` and print the values stored in `p["training"]` and `p["feedback"]`.

# %%

# %% [markdown]
# ---
# **Exercise**: Create a dictionary with `"condition": ["a", "b", "c"]"` and `"probability": [0.2, 0.2, 0.6]"` and write it to a file called `"config.json"` with `indent=4`:

# %%

# %% [markdown]
# Open `"config.json"` in your editor and manually add a field `"n_blocks":3` and save. Then, load the file into a dictionary called `config` and print the value stored in `config["n_blocks"]`:

# %%

# %% [markdown]
# ## 3. Configuring Visual Stimuli
#
# Now that we understand how to read and write config files, we can start to dive into PsychoPy which is the package we will use to present images and audio to and record responses from our subjects. In this section we will explore the presentation of visual stimuli with PsychoPy.
# A PsychoPy program usually starts by opening a `Window`, where images are shown to the subject.
# Just like our opened files, we can handle the `Window` using a context manager.
# This is very convenient because it prevents us from ending up with a frozen window - if our experiment crashes, the context manager will make sure that everything is cleaned up and the window is close.
# PsychoPy used a dual-buffer system which means that there are two screens: one that we are seeing and one that is hidden.
# When we draw images, we are always drawing to the hidden screen.
# The images are only revealed once we call `.flip()`.
#
#
# | Code                                                            | Description                                                   |
# | ---                                                             | ---                                                           |
# | `with Window() as win:`                           | Open a `Window` within a context manager                  |
# | `win.flip()`                                                    | Clear the screen and display new image                        |
# | `text = TextStim(win, text="Hi!")`                       | Create a text object for the given `Window`                   |
# | `rect = Rect(win, pos=(0,0), width=1, height=1, lineColor="white")` | Create a rectangle for the given `Window`                     |
# | `circle = Circle(win, radius=0.2, fillColor="blue")` | Create a circle for the given `Window`                     |
# | `rect.draw(), circle.draw(), text.draw()`                                                   | Draw a visual stimulus (e.g. rectangle) to the window buffer        |
# | `waitKeys()`                                                   | Wait until a key was pressed |
# | `waitKeys(keyList=["left", "right"])`                                                   | Wait until the left or right arrow key was pressed |

# %% [markdown]
# **Example**: Open a window within a context manager, then draw a white rectangle, `flip()` the window and wait for a key press 

# %%
with Window() as win:
    rect = Rect(win, lineColor="white")
    rect.draw()
    win.flip() # show the drawn rectangle
    waitKeys()

# %% [markdown]
# ---
# **Exercise**: Create a dictionary with, `"height":1`, `"width":1` and `"color":"white"` and write it to a file called `rect_config.json`

# %%

# %% [markdown]
# Read `rect_config.json` into a dictionary `cfg`, so that the code below, which shows a rectangle and waits for a key press, can be executed

# %%

# %%

with Window() as win:
    rect = Rect(win, height=cfg["height"], width=cfg["width"], lineColor=cfg["color"])
    rect.draw()
    win.flip() # show the drawn rectangle
    waitKeys()

# %% [markdown]
# Now modify `rect_config.json` by hand and set `"height":1.5`, `"width":0.75` and `"color":"pink"`, then rerun the cell above

# %% [markdown]
# ---
# **Exercise**: Create a dictionary with `"pos":(0, 0.5)`, `"color":"red"` and `"keys":["x", "m"]` and write it to a file `circle_config.json`

# %%

# %% [markdown]
# Read `circle_config.json` into a dictionary `cfg`
#

# %%

# %% [markdown]
# Modify the code below so it uses the values from `cfg` for the parameters `pos`, 'fillColor' and `keyList`

# %%
with Window() as win:
    circle = Circle(win, pos=(0,0), fillColor="white")
    circle.draw()
    win.flip()
    waitKeys(keyList=["space"])

# %% [markdown]
# Now modify `circle_config.json` in your editor and set `"pos":(0.2, -0.1)`, `"color":pink` and `"keys":["space"]`, then rerun the cell above.

# %% [markdown]
# ---
# **Exercise**: Create a dictionary with `"width":2`, `"height":2`, `"color":"teal"` and `"text":"Welcome!"` and  and write it to a file `text_config.json`

# %%

# %% [markdown]
# Read `text_config.json` into a dictionary `cfg`

# %%

# %% [markdown]
# Now write code that uses the parameters from `cfg` to do the following
# - open a `Window` within a context manager
# - draw a **rectangle** with `heigh=cfg["height"]`, `width=cfg["width"]` and `fillColor=cfg["color"]`
# - draw a **text stimulus** with `text=cfg["text"]`
# - `flip()` the window
# - wait for a key press. 

# %%

# %% [markdown]
# Now modify `text_config.json` in your editor and set `"height":1.9`, `"width":1.9` and `"text":"Hello!"`, then rerun the cell above.

# %% [markdown]
# ---
# **Exercise**: Create a dictionary that contains two other dictionaries `"circle":{"radius":0.1, "color":"magenta"}` and `"rect":{"height":1,"width":1, "color":"orange"}` and write it to a file `visual_config.json`

# %%

# %% [markdown]
# Read `visual_config.json` into a dictionary `cfg`, 

# %%

# %% [markdown]
# Now write code that uses the parameters from `cfg` to do the following:
# - open a `Window` within a context manager
# - draw a **rectangle** with `heigh=cfg["rect"]["height"]`, `width=cfg["rect"]["width"]` and `fillColor=cfg["rect"]["color"]`
# - `flip()` the window
# - wait for any key
# - draw a **circle** with `radius=cfg["circle"]["radius"]` and `fillColor=cfg["circle"]["color"]`
# - `flip()` the window again
# - wait for any key again.

# %%

# %% [markdown]
# Now modify `visual_config.json` in your editor and reduce the rectangle's width and height to **0.6** and increase the circle's radius to **0.3** and rerun the cell above.

# %% [markdown]
# ## 4. Refactoring an Experiment to Make it Configurable
#
# This folder contains a script called `posner_task.py` that contains an implementation of the [Posner cueing task](https://en.wikipedia.org/wiki/Posner_cueing_task), a classic psychophysical experiment that tests how spatial attention is deployed in a reaction task.
# Execute the cell below to run the experiment - the instructions will be displayed on screen.

# %%
# !python posner_task.py

# %% [markdown]
# **Exercise**: In the beginning of the script `posner_task.py`, multiple parameters are defined (e.g. `N_TRIALS`). Create a file called `posner_task_config.json` that stores these parameters. Then, modify `posner_task.py` so that it loads `posner_task_config.json` and replace the parameters with the values stored in the file. Modify `posner_task_config.json` to set the **number of trials** to 8, the **probability that a cue is valid** to 0.5 and the **cue duration** to 0.75 and rerun `posner_task.py`.

# %% [markdown]
# **Exercise**: Include the positions of the visual objects in `posner_task_config.json` and replace the values passed to the `pos` arguments with the values from that file. Modify the configuration so that the boxes and targets are displayed further to the left and right and rerun `posner_task.py` 
