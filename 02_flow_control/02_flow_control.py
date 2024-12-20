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

# %% [markdown] vscode={"languageId": "plaintext"}
# # Experimental Flow Control
#
# The structure of experiments has a certain flow: specific components must be executed repetitively a certain number of times and different things may have to happen depending on the state of the experiment. For example, an experiment may consist of multiple trials and depending on the response of the animal, we may or may not want to give a reward on any given trial.
# In this notebook we are going to explore the fundamental building blocks that allow us to translate this flow into code: loops and conditional expressions.

# %% [markdown] vscode={"languageId": "plaintext"}
# ## 1. Iterating trials
#
# Many programs contain components that must be repeated a certain number of times, like trials in experiments.
# `for` loops allow us to do exactly - they repeat code `for` a certain number of times.
# They work on sequences of data, like lists, pull out one value after another and then do something with that value.
# This is very close to our everyday language: if you are throwing a party and inviting your friends, you are essentially executing a loop:
# `for` every person in the list of people I know: invite that person to the party.
#
#
# | Code                                         | Description                                                          |
# | ---                                          | ---                                                                  |
# | `for letter in ["a", "b", "c"]:` <br> &nbsp;&nbsp;&nbsp;&nbsp; `print(letter)` | Print every `letter` in the list `["a", "b", "c"]`|
# | `for i in range(5):` <br> &nbsp;&nbsp;&nbsp;&nbsp; `print(i)` | Print every number `i` between 0 and 5 (not including 5)|
# | `for i in range(2, 7):` <br> &nbsp;&nbsp;&nbsp;&nbsp; `print(i)` | Print every number `i` between 2 and 7 (not including 7)|
# | `for i in range(1, 10, 2):` <br> &nbsp;&nbsp;&nbsp;&nbsp; `print(i)` | Print eververy **second** number `i` between 1 and 10 (not including 10)|
# | `for x_i in x:` <br> &nbsp;&nbsp;&nbsp;&nbsp; `print(x_i)` | Print every element `x_i` in the collection `x`|
#

# %% [markdown]
# **Exercise**: Write a for loop that prints the numbers **0** to **9**.

# %%

# %% [markdown]
# **Exercise**: Write a for loop that prints the numbers **5** to **10**.

# %%

# %% [markdown]
# **Excercise**: Write a for loop that counts from **0** to **100** in steps of **10**.

# %%

# %% [markdown]
# **Exercise**: Use a loop to print all `fruits` and their `colors`, for example `banana is yellow"`.

# %%
fruits = ["banana", "orange", "cherry"]
colors= ["yellow", "orange", "red"];

# %%

# %% [markdown]
# **Exercise**: Write a loop that prints the square of each element in `numbers`.
#

# %%
numbers = [4, 13, 56, 676];

# %%

# %% [markdown]
# **Exercise**: Write a loop that print out `"Run experiment for animal n"` for each animal id in the list below.

# %%
animal_ids = ["m23", "m59", "m145"];

# %%

# %% [markdown]
# **Excercise**: Use a `for` loop within another `for` loop to print `"This is block b"` for each block in `blocks` and <br>`"This is trial t"` for each t in `trials`.

# %%
blocks = [1, 2, 3]
trials = [1, 2, 3, 4, 5, 6, 7, 8 , 9 ,10];

# %%

# %% [markdown]
# ## 2. Conditional Expressions
#
# Another key component are conditional expressions. They allow us to write programs that behave differently under different circumstances.
# For example, under certain conditions in an experiment, you may want to give a reward or increase the difficulty of the task.
# An `if` statment can be accompanied by an `else` statement that tells the program what to do in case the `if` condition is not `True`.
# Additionally, the statement can have multiple `elifs`: other conditions that are only checked in case the `if` condition is not `True`.
# We could incorporate the `if` statement in our everyday example from the previous section and say:
# `for` every person in the list of people I know, `if` that person is a friend, invite that person to the party.
#
#
# ### Reference Table
#
# |Code|Description|
# |---|---|
# |`if x > 0:` <br> &nbsp;&nbsp;&nbsp;&nbsp; `print("positive")` <br> `elif x < 0:` <br> &nbsp;&nbsp;&nbsp;&nbsp; `print("negative")` <br> `else:` <br> &nbsp;&nbsp;&nbsp;&nbsp; `print("zero")`| Prints whether the number `x` is `"positive"`, `"negative"` or `"zero"`|
# | `x in [1, 2, 3]` | Returns `True` if the value of `x` appears in the list `[1,2,3]`|
# | `x==1 and y==0` | Returns `True` both expressions are `True` (i.e. `x` is 1 AND `y` is 0)|
# | `x==1 or y==0` | Returns `True` if AT LEAST one expression is `True` |
# | `not False` | Invert a boolean value (Returns: `True`) |
#

# %% [markdown]
# **Exercise**: Assign different values to `x` so that each `print` statement is executed once.

# %%
x = 20
if x > 10:
    print("High positive number")
elif x > 0:
    print("Small positive number")
elif x == 0:
    print("Zero!")
elif x < -10:
    print("Large negative number")
else:
    print("Small negative number")

# %% [markdown]
# **Exercise**: Add one `elif` statement to `print("This is a string")` when `x` is a string and one `elif` statement to `print("This is a float")` when `x` is a float. Assign different values to `x` so that each `print` statement is executed once.

# %%
x = "hi"
if isinstance(x, int):
    print("This is an integer")
else:
    print("I don't know what this is")

# %%

# %% [markdown]
# **Exercise**: Write an `if`/`else` statement that prints `"long"` when the list `zeros` is longer than 50 and `"short"` when it is shorter.

# %%
zeros = [0, 0, 0] *17;

# %%

# %% [markdown]
# **Exercise**: Write an if/else statement to print`"large value"` if the absolute value of
# a variable `x` is larger than 10 (i.e. it is greater than 10 OR smaller than -10). Execute this statement while setting x to **5** and **-13**.

# %%

# %% [markdown]
#  **Exercise**: Write an `if`/`else` statement that prints out `"small value"` if the absolute value of
#  x is smaller than 10 (i.e. it is smaller than 1 AND greater than -1). Execute this statement while setting x to **1.2** and **-0.5**.

# %%

# %% [markdown]
# **Exercise**: Use an `if`/`else` statement within a `for` loop to `print("vowel")` or `print("consonant")` for each letter in the list `letters`.

# %%
letters = ['w', 'q', 'x', 'k', 'g', 'm', 'f', 'i', 'w', 'j', 'h', 't', 'b', 'z', 'u', 'r', 'q', 'b', 'a', 'z']
vowels = ['a', 'e', 'i', 'o', 'u'];

# %%

# %% [markdown]
# **Exercise**: Use a `for` loop to iterate the list `play_tone` and an `if`/`else` statement to `print("silence...")` or `print("beep")` depending on whether the value in the list is True.

# %%
play_tone = [True, True, False, True, False, True, True, True];

# %%

# %% [markdown]
# **Exercise**: Use a `for` loop and `if`/`else` statement to determine whether each number in `numbers` is odd or even

# %%
numbers = [4, 18, 32, 13, 155, 56]

# %%

# %% [markdown]
# ## 3. Conditional Loops
#
# We can also combine loops and conditionals and create a procedure that is repeatedly executed for as long as a certain condition is `True`.
# This is exactly what `while` loops do.
# In an experiment, you may use them to wait while the subject is responding or to keep running the experiment until a certain finishing condition is met.
# Sticking to our party metaphor, we may say: `while` there are slices of pizza left, `if` you see a guest without pizza, offer them a slice of pizza.
#
# ### Reference Table
#
# |Code | Description                       |
# | --- | ---                               |
# |`while x>y`: <br> &nbsp;&nbsp;&nbsp;&nbsp; `print("x is bigger")` | Prints `"x is bigger"` as long as `x>y` is `True`|
# |`break`          | Exit the current loop |
# | `time.time()`   | Get the current time  |
# | `time.sleep(1)` | Wait for one second   |

# %% [markdown]
# **Exercise**: Run This cell. Then, change the value of `max_count` to **500** and run it again. Finally, change `True` to `False` and run a third time.

# %%
max_count = 100
count = 0
while True:
    count = count+1
    if count >= max_count:
        break
print("Ran " +str(count) +" iterations")

# %% [markdown]
# **Exercise**: Define a variable `n_trials=100` and write a `while` loop that subtracts 1 from `number_of_trials` until it is **0**.

# %%

# %% [markdown]
# **Exercise**: Define a variable `count=0` and use a `while` loop to add 1 to it as long as it is smaller than **60**.

# %%

# %% [markdown]
# **Exercise**: Write a `while` loop that does the same as the `for` loop defined below.

# %%
for i in range(0, 10):
    print(i)

# %%

# %% [markdown]
# ## 4. Advanced Iteration
#
# In some cases, we want to keep counting the number of iterations as we use a `for` loop to go through a list.
# This is what `enumerate()` does: it does not only return the elements in the sequence but also the number of each element in that sequence.
# Another useful tool is `zip()` which allows us to iterate through multiple sequences at once, for example: experimental conditions and stimulus intensities.
#
# ### Reference Table
# |Code | Description |
# | --- | ---         |
# | `for x_i, y_i in zip(x, y):` <br> &nbsp;&nbsp;&nbsp;&nbsp; `print(x_i, y_i)` | Prints every element `x_i` in `x` and every element `y_i` in `y`|
# | `for i, x_i in enumerate(x):` <br> &nbsp;&nbsp;&nbsp;&nbsp; `print(i, x_i)` | Print every element `x_i` and it's index `i` in the list `x`|
#

# %% [markdown]
# **Exercise**: Write a `for` loop with `zip` that prints each frequency and intensity in the lists `frequencies` and `intensities`.

# %%
frequencies = [600, 1000, 600, 1000]
intensities = [70, 70, 65, 65];

# %%

# %% [markdown]
# **Exercise**: What happens if the lists inside `zip()` do not have the same length?

# %% [markdown]
# **Exercise**: Use a `for` loop with `enumerate` to print each element in `conditions` as well as the index of that element in the list.

# %%
conditions = ["a", "b", "a ", "b", "c", "c"];

# %%

# %% [markdown]
# **Exercise**: Use `enumerate` to iterate the list below and print out every **second** name

# %%
names = ["Julia", "Matt", "Kyle", "Lisa"];

# %%

# %% [markdown]
# ## BONUS: Puzzles
#
# Even though the individual components we talked about are fairly simple, their interplay can produce a lot of complexity and allows us to achieve various things. This bonus section is intended to provide you with some challenging exercises that will put your knowledge of Python fundamentals to the test.

# %% [markdown]
# **Exercise**: Use `for` loops and `if` statements to find all prime number between 1 and 1000.

# %%

# %% [markdown]
# **Exercise**: Create a `while` loop that shuffles the list until there are no immediate repetitions of the same element

# %%
import random
x = [1, 2, 3, 4, 5] * 10
random.shuffle(x)  # randomize the list
print(x)


# %%
