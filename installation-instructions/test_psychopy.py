#!/usr/bin/env python
# coding: utf-8

# # Test PsychoPy
# 
# Welcome to the course! Execute the cell below to test PsychoPy is working.
# You should see a gray Window and some text appear.
# 

# In[1]:


from psychopy import visual
from psychopy.hardware import keyboard

kb = keyboard.Keyboard()
win = visual.Window(fullscr=False)
text = visual.TextStim(win, text="Welcome to the course!\n Press SPACE to exit")
text.draw()
win.flip()
kb.waitKeys(keyList=["space"])
win.close()

