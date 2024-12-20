# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.6
#   kernelspec:
#     display_name: psychopy
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Simulating an Experiment with Patching
# That we learned how to patch our code with mcck objects, we can apply our knowledge to simulate a full PsychoPy experiment. This folder contains a file called `experiment.py`. You can execute the cell below to run it!

# %%
# !python experiment.py

# %% [markdown]
# Open `experiment.py` in your editor and have a look at the code. Don't worry about the expression `if __name__=="__main__"` you see at the bottom. This hast the only purpose that, when the script is executed the way you just did, the function `main()` is called. Our aim is to patch this `main()` function to fully simulate this experiment so that it never executes any PsychoPy code and so that we can run it without having to manually press any buttons.

# %% [markdown]
# To start, create a script called `run_simulated.py` in the same folder as `experiment.py` and import the the `main` function from `experiment`. Now we can call this function using a context manager that patches a certain part of the module, for example:
#
# ```python
# with patch("experiment.core.wait"):
#     main()
# ```
#
# Will run `main()` while replacing the `core.wait` function with a mock that does nothing. The key is to provide the name of the function exactly as it is imported in the patched function. Since `experiment.py` uses `core.wait`, we have to define our patch target as `experiment.core.wait`.
# You can patch multiple things by combining multiple `patch()` calls in the context manager:
#
# ```python
# with patch("experiment.core.wait"), patch("experiment.core.quit"):
#     main()
# ```
#
# Just calling `patch()` will replace the function with a mock that does nothing. If we want to invoke a specific behavior, we can use `return_value` and `side_effect`:
#
# ```python
# with patch("experiment.core.wait", return_value="hi"), patch("experiment.core.quit", side_effect=my_mock):
#     main()
# ```
#
# In this example, whenever `main()` executes `core.wait()`, the value `"hi"` is returned and whenever it executes `core.quit` the function `my_mock` is called.

# %% [markdown]
# **Project**: Create a script that patches the `main()` function from `experiment.py` so that it runs fully automated without invoking any psychopy functionality. This means you have to patch the following functions and objects
#
# - The Window object
# - The TextStim object
# - The Sound.play methods
# - The core.wait function
# - the event.waitKeys function
#
# The simulated experiment should print `"beep"` whener `Sound.play()` is called and it should print `"wait for t"`, where t is the time waited for, when `core.wait()` is called. A call to `waitKeys` should return a randomly selected element of the provided `keyList` and a random response time if `timeStamped` is `True`.
# Howver, you may start by just replacing all of the above component with regular mocks that do nothing and then start to include the described functionality.
