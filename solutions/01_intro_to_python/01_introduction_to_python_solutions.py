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
# # Introduction to Python
#
# Welcome to the course!
# Our aim is to develop robust experiment applications in Python and use structured approaches and techniques for programming that make our lives easier.
# We start our journey by building or revising our fundamental knowledge of Python.
# This notebook focuses on how to represent and manipulate different kinds of data using basic Python operations.

# %% [markdown]
# ## 1. Data Types and Variables
#
# Programs receive, create and operate on data.
# There are many different types but a few **essential** ones can be found in most programming languages.
#  In Python, they are called:
#
# - **int**: integers or non-decimal numbers, example -7, 0, 101
# - **float**: floating-point numbers with a limited number of decimal places, for example: 0.1, pi, 1/3
# - **str**: a string of characters, marked by quotations, for example "a", "13", "hello"
# - **bool**: boolean logical values, can be either True or False
#
# The type determines the range of **values** the data can take on as well as the set of **operations** that can be performed on them (more on this in the next section).
# For each type there is a function with the same name that converts data to that type.
# For example `int(x)` converts the value of `x` to an integer --- this is known as **type casting**.
#
#
# ### Reference Table
# | Code                | Description                                                                                    |
# | ---                 | ---                                                                                            |
# | `x = 3`             | Assign the integer number `3` to the variable `x`                                              |
# | `x = 3.14`          | Assign the floating number `3.14` to the variable `x`                                          |
# | `x = "hi"`          | Assign the string `"hi"` to the variable `x`                                                   |
# | `x = True`          | Assign the boolean value `True` to the variable `x`                                            |
# | `type(x)`           | Get the data type of variable `x`                                                              |
# | `int(x)`, `float(x)`, `str(x)`, `bool(x)` | Convert the variable `x` to an integer, float, string, boolean  |

# %% [markdown]
# **Exercise**: Determine the type of `x`

# %%
a = 123;

# %%
# Solution
type(a)

# %% [markdown]
# **Exercise**: Determine the type of `ok`

# %%
ok = True;

# %%
# Solution
type(ok)

# %% [markdown]
# **Exercise**: Convert `n_trials` to a float

# %%
n_trials = 13;

# %%
# Solution
float(n_trials)

# %% [markdown]
# **Exercise**: Convert `percent` to a string

# %%
percent = 0.75;

# %%
# Solution
str(percent)

# %% [markdown]
# **Exercise**: Convert `nothing` to a boolean

# %%
nothing = "";

# %%
# Solution
bool(nothing)

# %% [markdown]
# **Exercise**: Create a boolean variable that is `False` and convert it to an integer

# %%
# Solution
x = False
int(x)

# %% [markdown]
# **Exercise**: Create a float variable that is `0.001` and convert it to a string

# %%
# Solution
x = 0.001
str(x)

# %% [markdown]
# **Exercise**: Create a string variable `"Hello"` and convert it to a boolean

# %%
# Solution
x = "Hello"
bool(x)

# %% [markdown]
# ## 2. Operators
#
# Operators are special symbols or keywords that perform operations on values and variables.
# They're the basic tools Python uses to work with data.
# One important class are arithmetic operators, like `+` and `*`.
# In some situations, these behave as you would expect: for example, adding two numbers computes their sum.
# However, sometimes they do things that may be unexpected: for example, adding two strings concatenates them.
# Some combinations of data types an operators are not defined at all: for example, you can't subtract one string from another.
# Another important class are comparisons such as `<` or `==`.
# These allow us to ask: is one value greater, smaller or the same as another one, and they always return either `True` or `False`.
#
# ### Reference Table
#
# |Code                             |Description                                                         |
# |---                              |---                                                                 |
# |`x+y`,`x-y`,`x/y`, `x*y`         | Add, subtract, divide, multiply two numbers `x` and `y`            |
# | `x<y`, `x>y`, `x==y`, `x!=y`    | Check whether `x` is smaller, larger, equal to, not equal to `y`   |
# | `x<=y`, `x>=y`                  | Check whether `x` is smaller than or equal to, larger than or equal to `y` |
# | `"Psycho"+"Py"`                 | Concatenate the two strings (result: `"PsychoPy"`)                 |
# | `"pew" * 2`                     | Repeat the string two times (result: `"pewpew"`)                   |
# | `9 ** 2`                        | Square the number `9` (result: `81`)                               |
# | `7 % 3`                         | Get the remainder of dividing `7` by `3` (result: `1`)             |

# %% [markdown]
# **Exercise**: Add `134` and `4721`

# %%
# Solution
134+4721

# %% [markdown]
# **Exercise**: What is the remainder of dividng 13 by 5?

# %%
# Solution
13 % 5

# %% [markdown]
# **Exercise**: What is `567` squared?

# %%
# Solution
567**2

# %% [markdown]
# **Exercise**: Concatenate the two strings

# %%
x = "Hello"
y = "World";

# %%
# Solution
x+y

# %% [markdown]
# **Exercise**: What is the data type of the result from dividing `6` by `2`

# %%
# Solution
type(6/2)

# %% [markdown]
# **Exercise**: What is larger? 23 times 81 or 44 squared?

# %%
# Solution
(23*81) > 44**2

# %% [markdown]
# **Exercise**: Divide 28 by the sum of 3 and 5

# %%
# Solution
28 / (3+5)

# %% [markdown]
# **Exercise**: Repeat the string below 3 times

# %%
he = "He";

# %%
# Solution
he * 3

# %% [markdown]
# **Exercise**: Which string value is larger, `"a"` or `"b"`?

# %%
# Solution
"a" > "a"

# %% [markdown]
# **Exercise**: Can `N` be evenly divided by 3?

# %%
N =35624;

# %%
# Solution
N%3 == 0

# %% [markdown]
# ## 3. Lists
#
# Often, we want to represent not only a single datum but collections of data.
# The `list` is a datatype that allows us to do exactly that.
# Think of lists as a container that can hold any kind of data --- even other lists.
# Since lists are ordered we can also access specific elements of the list by providing their indices.
# One think to keep in mind is that Python starts to count at 0 so `x[0]` will return the 1st element of a list and `x[1]` will actually return the second one.
#
# ### Reference Table
# |Code|Description|
# |---|---|
# | `x = [7, 1, 4]` | Define a list containing three values |
# | `[2, 3] + [1]` | Concatenate two lists (result: `(2,3,1)`)|
# | `[1] * 3`      | Repeat the list (result: `[1,1,1]`)|
# | `x[-1]`       | Get the last element of `x`   |
# | `x[2:5]`      |  Get the 3rd, 4th and 5th element of `x`|
# | `x[1:]`       | Get all elements of `x`, except the first |
# | `x.append(1)` |  Append the number `1` to the list `x`|
# | `len(x)` | Get the length (i.e. number of elements in) a tuple or list `x`| 
# | `sum(x)`  | Get the sum of a tuple or list `x` |
#

# %% [markdown]
# **Exercise**: Create a list that contains the numbers 1, 2, and 3

# %%
# Solution
x = [1, 2, 3]

# %% [markdown]
# **Exercise**: Concatenate the two lists defined below

# %%
weekdays = ["mo", "tue", "wed", "thu", "fr"]
weekend = ["Sa", "Sun"];

# %%
# Solution
weekdays + weekend

# %% [markdown]
# **Exercise**: Append the next number `8` to the `fibonacci` list

# %%
fibonacci = [0, 1, 1, 2, 3, 5];

# %%
# Solution
fibonacci.append(8)

# %% [markdown]
# **Exercise**: Get the length of the list of `zeros` defined below

# %%
zeros = [0, 0, 0, 0] * 23;

# %%
# Solution
len(zeros)

# %% [markdown]
# **Exercise**: What is the sum of the list `true_and_false`?

# %%
true_and_false = [True, False, False, True, True, True];

# %%
# Solution
sum(true_and_false)

# %% [markdown]
# **Exercise**: Get the 3rd element of the `dice_numbers` list

# %%
dice_numbers = [1, 2, 3, 4, 5, 6];

# %%
# Solution
dice_numbers[2]

# %% [markdown]
# **Exercise**: Get all letters of the `alphabet` except for `"z"`

# %%
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];

# %%
# Solution
alphabet[:-1]

# %% [markdown]
# **Exercise**: Create a list of 100 zeros

# %%
# Solution
[0,0] * 5

# %% [markdown]
# **Exercise**: Which of the two lists defined below is longer?

# %%
x = [4, 2, 5, 6, 7] * 7
y = [1, 3, 4] * 11;

# %%
# Solution
len(x) > len(y)

# %% [markdown]
# ## BONUS: Puzzles
#
# Here is a little bonus section that lets you explore some more intricate details of data types and operators and see some ways in which they can produce unexpected results.

# %% [markdown]
# **Excercise**: Compute the square root of 1156 using only the operators introduced in this notebook

# %%
# Solution
1156 ** (1/2)

# %% [markdown]
# **Excercise**: What percentage of Elements in the list below is `True`?

# %%
was_hit = [True, False, True, True, False, False, True, False, False, True, False, False, False, True];

# %%
# Solution
sum(was_hit)/len(was_hit)*100

# %% [markdown]
# **Exercise**: What happens if you convert a boolean value `False` to a `str` and then back to a `bool`?

# %%
# Solution
bool(str(False))

# %% [markdown]
# **Exercise**: Check if `0.1 + 0.2` is equal to `0.3`:

# %%
# Solution
print(0.1 + 0.2 == 0.3)  # False

# %% [markdown]
# **Excercise**: Compute the square root of 1156 using only the operators introduced in this notebook

# %%
list_of_lists = [[[3], [1]], [[2]]]

# %%
# Solution
list_of_lists[0][1][0]
