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
# # Creating Reusable Experiments with Command Line Interfaces
#
# In the previous session, we learned how to use configuration files to make our experiments more reusable. However, this approach still requires us to change something when we want to change the behavior of the experiment, namely the configuration file. What if there are parameters that I want to change regularly, maybe even on every single run of the experiment (e.g. the subject ID). Always changing the config file does not seem like a good strategy for that.
# This is where command line interfaces (CLIs) come into play. A CLI provides an easy and convenient way to pass parameters to our program by simply typing the name of the program and, next to it, the values we want to put in. In this notebook, we will learn how to build powerful CLIs that make our programs even more reusable!

# %%
# %pip install psychopy

# %%
from argparse import ArgumentParser
from psychopy import prefs
prefs.hardware['audioLatencyMode'] = 0  # prevent psychtoolbox from taking over the sound card
from psychopy.event import waitKeys
from psychopy.sound import Sound
from psychopy.visual import Window
Sound(stereo=False);  # avoid bug that results from automatically setting `stereo`

# %% [markdown] vscode={"languageId": "plaintext"}
# ## 1. Creating an Argument Parser
#
# An argument parser takes in arguments from the command line and feeds them into our Python program.
# Python has a builtin module called `argparse` that does this for us.
# Let's assume we have a CLI program that adds two numbers.
# To call this program we would type in our terminal something like that `python add.py 3 2`, where `add.py` is the name of the program and `3` and `2` are the values provided to the CLI.
# However, it would be annoying to constantly jump between our editor and the terminal.
# Fortunately, argparse has a method of directly providing the `args` as if we were calling the program from the terminal.
# This gives us a convenient way for writing and testing our scripts in the same interface.
# In this section we are  going to write CLI scripts that allow us to play different sounds using PsychoPy's `Sound` class.
#
# ### Reference Table
#
# | Code                                            | Description |
# | :---------------------------------------------- | :---------- |
# | `parser = ArgumentParser()`                 | Create a parser for command line arguments |
# | `parser.add_argument("x", type=int)`        | Add an integer argument `"x"` to the parser |
# | `parser.add_argument("y", type=str)`        | Add a string argument `"y"` to the parser |
# | `parser.print_help()`                                              | Print the help documentation of the `parser`            |
# | `args = parser.parse_args(args=["3", "y"])` | Parse the arguments and set the `"x"` to `"3"` and `"y"` to `"hi"`|
# | `args.x`                                    | Access the value passed to the argument `"x"`             |
# | `tone = Sound()`                         | Create a pure tone |
# | `tone = Sound(value=800)`                | Create a pure tone with a frequency of `800` Hz |
# | `tone = Sound(secs=1.5)`                 | Create a pure tone with a duration of `1.5` seconds |
# | `tone = Sound(hamming=True)`              | Create a sound where the onset and offset are smoothly ramped up/down using a hamming window |
# | `tone.play()`              | Play the sound |

# %% [markdown]
# ---
# **Example**: Make a parser that accepts integers for `n_trials`:

# %%
parser = ArgumentParser()
parser.add_argument("n_trials", type=int)
parser.print_help()

# %% [markdown]
# Make `args` from the `parser` above, with `args.n_trials` set to `10`:

# %%
args = parser.parse_args(args=["10"])
args.n_trials

# %% [markdown]
# Make `args` from the `parser` above, with `args.n_trials` set to `18`:

# %%
args = parser.parse_args(args=["18"])
args.n_trials

# %% [markdown]
# ---
# **Exercise**: Make a parser that accepts integers for `n_blocks`:
#
#

# %%

# %% [markdown]
# Make `args` from the `parser` above, with `args.n_blocks` set to `2`:

# %%

# %% [markdown]
# Make `args` from the `parser` above, with `args.n_blocks` set to `5`:

# %%

# %% [markdown]
# ---
# **Exercise**: Make a parser that accepts strings for `subject`:
#

# %%

# %% [markdown]
# Make `args` from the `parser` above,  with `args.subject` set to `Fred`:

# %%

# %% [markdown]
# Make `args` from the `parser` above,  with `args.subject` set to `Julia`:

# %%

# %% [markdown]
# ---
# **Exercise**: Make a parser that accepts integers for `freq`:

# %%

# %% [markdown]
# Make PsychoPy play a sound at **800** Hz when `args.freq` is set to `800`:

# %%

# %% [markdown]
# Make Psychopy play a sound at **1200** Hz when `args.freq` is set to `1200`:

# %%

# %% [markdown]
# ---
# **Exercise**: Make a parser that accepts integers for `freq` and `dur`:

# %%

# %% [markdown]
# Make PsychoPy play a **500** Hz tone with a duration of **1.8** seconds with `args` from the `parser` above, when `args.freq` set to `500` and `args.secs` set to `1.8`:

# %%

# %% [markdown]
# Make PsychoPy play a **4000** Hz tone with a duration of **0.25** seconds with `args` from the `parser` above, when `args.freq` set to `4000` and `args.secs` set to `0.25`:

# %%

# %% [markdown]
# ---
# **Exercise**: Make a parser that accepts integers for `freq` and booleans for `hamming`:

# %%

# %% [markdown]
# Make PsychoPy play a **330** Hz tone with onset and offset ramp with `args` from the `parser` above, when `args.freq` is set to `330` and `args.hamming` set to `True`:

# %%

# %% [markdown]
# Make PsychoPy play a **950** Hz tone without onset and offset ramp with `args` from the `parser` above, when `args.freq` is set to `950` and `args.hamming` set to `False`:

# %%

# %% [markdown]
# ## 2. Documenting your CLI
#
# Adding arguments to a CLI can make a program more versatile but also harder to understand.
# To make our program easy to use, we can provide documentation that explains what the program and the individual parameters are doing.
# We can also use named arguments where each value is preceded by an identifier like `python add.py --num1 3 --num2 5`.
# This makes it easier to understand what each parameter does, and it also allows us to pass in the parameters in any order.
# Its important to keep in mind that named arguments are **optional**, so our program has to be able to run without them!
# In this section, we are exploring some advanced CLI functions together with PsychoPy's `waitKeys` functions that allows us to record responses using a keyboard.
# Even though we won't show any images, we'll still have to open a `Window` because PsychPy will only record keys from an active window.
#
#
# ### Reference Table
# | Code                                                                   | Description |
# | :--------------------------------------------------------------------- | :---------- |
# | `parser = ArgumentParser(description="This program ...")`    | Create an argument parser and add a `description` about the program|
# | `parser.add_argument("n", help="This argument...")`        | Add a positional argument `"n"` and add a `help` text about the argument             |
# | `parser.add_argument("--sub", type=str)`                           | Add an optional named argument `"--sub"` of type string             | 
# | `parser.add_argument("--train", action="store_true")`                 | Add an optional named argument `"--train"` that, when included, takes the value `True`             |
# | `args = parser.parse_args(args=["--sub", "Bob", "--train"])` | Parse the arguments and set `args.sub` to `"Bob"` and `args.train` to `True`             | 
# | `with Window() as win:`                           | Open a `Window` within a context manager (required for recording key presses)                 |
# | `keys = waitKeys()`                                | Wait until any key is pressed |
# | `keys = waitKeys(keyList=["a", "b"])`              | Wait until the keys `"a"` or `"b"` are pressed | 
# | `keys = waitKeys(maxWait=3)`                       | Wait until any key is pressed or `3` seconds passed |
# | `keys = waitKeys(timeStamped=True)`                | Wait until any key is pressed and return the time of the event |
#

# %% [markdown]
# **Example**: Make an argument parser that accepts strings for `--key1` and `--key2`

# %%
parser = ArgumentParser()
parser.add_argument("--key1", type=str)
parser.add_argument("--key2", type=str)
parser.print_help()

# %% [markdown]
# Make PsychoPy wait until the keys **q** or **p** were pressed with `args` from the `parser` above, when `args.key1` is set to `"q"` and `args.key2` set to `"p"` and print the recorded key:

# %%
args = parser.parse_args(args=["--key1", "q", "--key2", "p"])
with Window() as win:
    keys = waitKeys(keyList=[args.key1, args.key2])
keys

# %% [markdown]
# Make PsychoPy wait until the **return/enter** key was pressed with `args` from the `parser` above, when `args.key1` is set to `"return"` and `args.key2` is not used at all:

# %%
args = parser.parse_args(args=["--key1", "return"])
with Window() as win:
    keys = waitKeys(keyList=[args.key1, args.key2])
keys

# %% [markdown]
# ---
# **Exercise**: Make an argument parser that accepts strings for `--yes` and `--no` 

# %%

# %% [markdown]
# Make PsychoPy wait until the keys **y** or **n** were pressed with `args` from the `parser` above, when `args.yes` is set to `"y"` and `args.no` is set to `"n"`:

# %%

# %% [markdown]
# Make PsychoPy wait until the key **space** was pressed with `args` from the `parser` above, when `args.yes` is set to `"space"` and `args.no` is not used at all:

# %%

# %% [markdown]
# ---
# **Exercise**: Make an argument parser and add the description: **"This program waits until 'maxwait' has passed or the 'key' was pressed"**.
# Make the parser accept strings for `"--key"` and add the help: **"Wait for this key"**.
# Also make the parser accept floats for `"--maxwait"` and add the help: **"Maximum time to wait in seconds"**:

# %%

# %% [markdown]
# Make PsychoPy wait until the key **z** was pressed or **2.5** seconds passed with `args` from the `parser` above, when `args.key` is set to `"z"` and `args.maxwait` is set to `"2.5"`:

# %%

# %% [markdown]
# Make PsychoPy wait until the key **g** was pressed or **3.25** seconds passed with `args` from the `parser` above, when `args.key` is set to `"g"` and `args.maxwait` is set to `"3.25"`:

# %%

# %% [markdown]
# ---
# **Exercise**: Make an argument parser that accepts strings for `"--key"` and add a `"--timed"` flag with `action="store_true"`:

# %%

# %% [markdown]
# Make PsychoPy wait until the key **space** was pressed with `args` from the `parser` above when `args.key` is set to `"space"` and return the time at which the key was pressed `if args.timed == True`:

# %%

# %% [markdown]
# Make PsychoPy wait until the key **space** was pressed with `args` from the `parser` above when `args.key` is set to `"space"` and don't return the time at which the key was pressed if the `"--timed"` flag was not included:

# %%

# %% [markdown]
# ---
# **Exercise**: Make an argument parser that accepts strings for `"--left"` and `"--right"` and add a `"--wait"` flag with `action="store_true"`:

# %%

# %% [markdown]
# Make PsychoPy wait until the **left** or **right** arrow key was pressed if `args.left="left"` and `args.right="right"` but only wait `if args.wait==True`:

# %%

# %% [markdown]
# Execute the code from above again but without waiting by omitting `"--wait"` flag from `"args"`.

# %%

# %% [markdown] vscode={"languageId": "plaintext"}
# ## 3. Writing a program with a command line interface
#
# Now we know how to write CLIs, play Sounds and record Responses - Let's create some progamms.
# In this section you are going to create new files to write your scripts in.
# Make sure that you place the files in the same folder as this notebook (4_command_line_interface), so Python will be able to find them!
# To run a program from the terminal, simply write `!` before its name and execute the notebook cell. 
#
# **IMPORTANT**: By running this notebook, PsychoPy connected to your audio device. As long as this connection is activte you will not be able to run other PsychoPy programs that also need to communicate with your audio interface. Thus, before you continue, make sure that you click the **Restart** button at the top your VSCode editor to let go of any existing connection.
#
# #### Reference Table
#
# |Code | Description |
# |---|---|
# |`!python some_program.py -h` | Print the help documentation of `some_program`'s command line interface |
# |`!python some_program.py hi` | Execute `some_program.py` with `hi` as the first positional argument |
# |`!python some_program.py hi --arg1 2` | Execute `some_program.py` with `hi` as the first positional argument and `2` as the value of the optional argument `--arg1` |

# %% [markdown]
# **Exercise**: Call the help of the Python program `say_hi_to.py`

# %%

# %% [markdown]
# **Exercise**: Use `say_hi_to.py` to say hi to **"John Doe"**

# %%

# %% [markdown]
# **Exercise**: Use `say_hi_to.py` to say hi to shout **"HI BOB!"**

# %%

# %% [markdown]
# ---
# **Exercise**: Write a program called `react_to_tone.py` with an `ArgumentParser` that 
# - accepts a string argument `key`, an integer argument `freq` and a `--timed` flag
# - plays a tone at the frequency given by `--freq`
# - waits fo the `key` and prints the value returned by `waitKeys()`
# - prints the time at which the key was pressed if the `--timed` flag was included.
#  
# Then, execute the cell below to make `react_to_tone.py` play a 600 Hz tone and wait until y was pressed.

# %%
# !python react_to_tone.py 600 y

# %% [markdown]
# Make `react_to_tone.py` play a **750 Hz** tone and wait until the key **n** was pressed and return the **time** the key was pressed:

# %%

# %% [markdown]
# ---
# **Exercise**: Write a program called `change_pitch.py` with an ArgumentParser that
# - accepts integers for `freq`, `step` and `n_trials`
# - plays tones starting at the frequency `freq` using a loop with `for i in range(args.n_trials)`
# - waits, after every tone, until the `"up"` or `"down"` key was pressed
# - decreases the tone frequency by `step` if `"down"` was pressed and increases it `step`, if `"up"` was pressed
#
# Then, execute the cell below to make `change_pitch.py` play **10** tones, starting at **1200** Hz with a step size of **50** Hz

# %%
# !python change_pitch.py 1200 50 10

# %% [markdown]
# Make `change_pitch.py` play **5** tones, starting at **2100** Hz with a step size of **100** Hz

# %%

# %% [markdown]
# ## 4. Combining CLI and Configuration Files
#
# Now we can combine CLIs and configuration files to get the best of both worlds: We can use CLIs to pass in parameters that we want to change all of the time and configuration files to store the parameters that we don't want to change as often.
# The program that is executed below runs a pure tone audiogram to detect the hearing threshold at a given frequency, a perfect use case to combine CLIs and config files!

# %%
# !python pure_tone_audiogram.py

# %% [markdown]
# **Exercise**: In the beginning of the script `pure_tone_audiogram.py`, multiple parameters are defined (e.g. `FREQUENCY`). You have to
# - create a file called `audiogram_config.json` that stores these parameters
# - modify `pure_tone_audiogram.py` so that it loads `audiogram_config.json` and replace the parameters with the values stored in the file
# - change the **start volume** to 0.5 and the **number of reversals** to 6 
# - rerun `pure_tone_audiogram.py`

# %% [markdown]
# Now add add an `ArgumentParser` to `pure_tone_audiogram.py` that accepts strings for `--config_file` and use the value of `args.config_file` as path when loading the configuration file. Write a new file called `audiogram_config2.json` and change the **frequency** to **2000** Hz. Then, execute the cell below to run `pure_tone_audiogram.py` with the new configuration.

# %%
# !python pure_tone_audiogram.py --config_file audiogram_config2.json

# %% [markdown]
# Add a `--frequency` argument to the parser and use this argument instead of the value stored in the configuration file to set the `value` of the tone so that the cells below run the audiogram with different frequency

# %%
# !python pure_tone_audiogram.py --config_file audiogram_config2.json --frequency 600

# %%
# !python pure_tone_audiogram.py --config_file audiogram_config2.json --frequency 1250
