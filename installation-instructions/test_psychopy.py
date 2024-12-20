# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.6
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Test PsychoPy
#
# Welcome to the course! Execute the cell below to test PsychoPy is working.
# You should see a gray Window and some text appear.
#

# %%
from psychopy import visual
from psychopy.hardware import keyboard

kb = keyboard.Keyboard()
win = visual.Window(fullscr=False)
text = visual.TextStim(win, text="Welcome to the course!\n Press SPACE to exit")
text.draw()
win.flip()
kb.waitKeys(keyList=["space"])
win.close()
