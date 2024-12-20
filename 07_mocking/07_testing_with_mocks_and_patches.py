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

# %%
from unittest.mock import Mock, patch

# %%

# %% [markdown]
# ## Making Code More Testable: Utilizing Mocks and Patches in pytest

# %% [markdown]
# Some code is particularly challenging to test, either because it is:
#   - unpredictable (e.g. functions with random stochastic steps),
#   - dependent on access to private or large data files,
#   - computationally slow,
#   - depends on other systems out of our control.
#
# How can we ensure that the code we write works the way it does in these cases?  We can **"Mock"** out the difficult-to-test parts!

# %% [markdown]
# ---

# %% [markdown]
# ### Mocking to Create Predictable Behavior
#
# While we can write custom functions using the `def` keyword, we can also use Object-Oriented Programming to create objects that *behave* as though they were functions, even if they really aren't doing any computation at all.  The `Mock` class from the built-in `unittest` library makes it convenient for creating these "Mock" (sometimes called "Fake") objects.  
#
# In this section, we'll get familiar with how `Mock` objects work, which we'll use in the sections following to get tough-to-test code under control.
#
# | Code | Description |
# | :- | :- |
# | **`mock = Mock()`** | Create a Mock() object |
# | **`mock(1, 2)`** | Call the mock object as though it were **any function you want**. Doesn't actually do anything. |
# | **`mock.return_value = 5`** | Tell the mock function to always return `5` when called, no matter the inputs. |
# | **`mock.some_method(3, 5)`** | Call **any method you want** on the mock object. Doesn't actually do anything.|
# | **`mock.some_method.return_value = 10`** | Tell the `some_method` mock method to always return `10` when called, no matter the inputs. |
#

# %% [markdown]
# **Example**: Create a `five` Mock object that passes the tests below:

# %%
five = Mock()
five.return_value = 5

# %%
assert five(3) == 5
assert five(1, 2, 3) == 5
assert five('Hi Everyone!') == 5

# %% [markdown]
# **Exercise**: Create a `three` Mock object that passes the tests below:

# %%

# %%
assert three(1, 2, 3) == 3
assert three([10, 20]) == 3
assert three('two', 'one') == 3

# %% [markdown]
# **Exercise**: Create a `data` Mock object that passes the tests below:

# %%

# %%
assert data.mean() == 10.5
assert data.std() == 5.2

# %% [markdown]
# **Exercise**: The `random` module has functions that are difficult to predict what they will do.  Let's fix that by creating a `random` Mock object that is more predicatable, that passes the tests below:

# %%

# %%
assert random.randint() == 42
assert random.randint(1, 100) == 42
assert random.randfloat() == 3.14

# %% [markdown]
# **Exercise**: The `load(filename)` function from `json` needs a data file in order to work. Let's make it easier to simulate data by creating a `load` Mock object that always gives us a specific simulated dataset:

# %%

# %%
assert load() == {'a': 3, 'b': 4}

# %% [markdown]
# ---

# %% [markdown]
# ### Mocking to Spy on your Code
#
# How are the functions and objects actually being used inside your code?  By adding `Mock` features to a Python object with `wraps`, the object will continue to work the same as before, but now you can test how it is used inside other pieces of code!  This is called making a **Spy**, and is a valuable technique for testing complex code pipelines.
#
# | **Code** | **Description** |
# | :-- | :-- |
# | **`spy = Mock(wraps=print)`** | Wrap the `print()` function, so you can find out how it was called. |
# | **`args, kwargs = spy.call_args`** | Find out what positional and keyword arguments were used when calling the spy` |
# | **`spy.assert_called()`** | Raises an `AssertionError` if `spy` was never called. |
# | **`spy.assert_called_once()`** | Raises an `AssertionError` if `spy` was called more or less than once. |
# | **`assert spy.call_count == 5`** | Raises an `AssertionError` if `spy` wasn't called exactly `5` times. |
# | **`spy.assert_called_with('hello')`** | Raises an `AssertionError` if `spy` was not last called with `'hello'` as the input. |
#

# %% [markdown]
# **Example**: Run the code below, and test the following:
#   - Was `mock_print()` only called one time?
#   - Was `mock_print()` called with the positional argument: 'Hello, World'?

# %%
mock_print = Mock(wraps=print)
mock_print('Hello, World')

# %%
mock_print.assert_called_once()
mock_print.assert_called_with('Hello, World')

# %% [markdown]
# **Exercise**: Run the code below, and test the following:
#
#   - Was `mock_rnd` called at least once?
#   - Was `mock_rnd` called exactly twice?
#   - Was `mock_rnd` last called with the positional arguments `10` and `100`?

# %%
import random
mock_rnd = Mock(random.randint)
mock_rnd(1, 10)
mock_rnd(10, 100)

# %%

# %% [markdown]
# **Exercise**: Is `record_data()` writing data to `mydata1.txt`, as expected?  run the function with a `Mock` object instead of the `save_fun` to spy on the function and check the call arguments to `save_fun` start with `mydata1.txt` (Hint: `spy.call_args[0][0] == 'mydata1.txt'`)

# %%
import numpy as np

def record_data(save_fun = np.savetxt):
    save_fun('mydata1.txt', [1, 2, 3])


# %%

# %% [markdown]
# **Exercise**: The function `wait_n_seconds(n)` is special: it should be calling it's `sleep()` function (which is `time.sleep()`, by default) 10 times for every second that the function is supposed to wait, and wait 100 milliseconds each call.  Let's test this by replacing the `sleep` function with a `Mock()` and testing that:
#   - `wait_n_seconds(1)` calls the sleep function 10 times.
#   - `wait_n_seconds(2)` calls the sleep function 20 times.
#   - `wait_n_seconds(0)` never calls the sleep function.

# %%
import time

def wait_n_seconds(n, sleep=time.sleep):
    ms = n * 1000
    while ms > 0:
        ms = ms - 100
        sleep(0.1)

wait_n_seconds(1)


# %%

# %% [markdown]
# ---

# %% [markdown]
# ### Patching to Make a Mock
#
# It is convenient to Mock an input to a function or an object, but sometimes the code you want to Mock isn't so easily accessible. This is where `unittest.mock.patch()` comes in!  Using a `with` block, you can tell python to swap out the code from one module with a mocked version during some specified period.  Below is the pattern:
#
# ```python
# with patch('module.fun') as mock:
#     run_code()
# ```

# %% [markdown]
# **Example**:  Below is the `wait_n_seconds()` function again, but this time there is no way to override the `time.sleep()` function it calls through the inputs.  Without changing the `wait_n_seconds()` function, use `patch` to make it so calling `wait_n_seconds(1000)` runs in no time!

# %%
def wait_n_seconds(n):
    import time
    ms = n * 1000
    while ms > 0:
        ms = ms - 100
        time.sleep(0.1)


# %%
# Turns time.sleep into a Mock object.
with patch('time.sleep') as mock_sleep:   
    wait_n_seconds(1000)


# %% [markdown]
# **Exercise**: Below is the `am_i_lucky()` function, which returns `True` if the random number generator `random.randint` happens to return the number `42`.  Without changing the `am_i_lucky()` function, use `patch` to make it so you are lucky every time!

# %%
def am_i_lucky():
    random_num = random.randint(1, 100000)
    if random_num == 42:
        print('You win!')
        return True
    else:
        print('You lose.`')
        return False
    


# %%

# %% [markdown]
# **Exercise**: Below is the function `get_area_of_circle()`, which uses `estimate_pi()` to work.  The only problem is, the `estimate_pi()` function is really slow!  Without changing either of the functions, use `patch` to:
#   - Make `get_area_of_circle()` run very quickly.
#   - Test that the `get_area_of_circle()` function works exactly correctly (i.e. it calcules $area = \pi r^2 $)
#
# Hint: `patch()` requires a module name in order to work.  to patch a function in the main namespace (i.e. not in another library), the module name is `__main__` (e.g. `__main__.estimate_pi`)

# %%
def get_area_of_circle(radius):
    pi = estimate_pi()
    area = pi * radius ** 2
    return area


def estimate_pi():
    inside_circle, num_samples = 0, 4000000
    for _ in range(num_samples):
        x, y = random.uniform(-1, 1), random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            inside_circle += 1
    return 4 * inside_circle / num_samples


# %%

# %% [markdown]
# ## 4. Patching with Side Effects
#
# Sometimes, we a mock that does not just return the same value all of the time but actually does something with the parameters that are passed to the mocked function. This is were side effects come in. Where a `return_value` provides a constant value for a function, a `side_effect` provides another function that is called instead of the mocked code. With side effects, we can define our mocks so that they behave similarly to the real code they are patching and make sure they produce the outputs that are expected by other parts of our program.
#

# %% [markdown]
#
# **Example**: Below is the wait_n_seconds() function we patched before. However, earlier we simply replaced time.sleep with a mock that did nothing. Now, we want to replace it with another function that, instead of actually waiting just prints out the duration we would have waited.

# %%
def wait_n_seconds(n):
    import time
    ms = n * 1000
    while ms > 0:
        ms = ms - 100
        time.sleep(0.1)


# %% [markdown]
# To do this we can create a new function `print_sleep` that takes in a value `t` and prints `"sleeping for t"`. Then we pass this function as a side_effect to our mock. Now our function is executed when the mock is called so that when `wait_n_seconds()` calls `time.sleep(0.1)` it actually executes `print_sleep(0.1)`

# %%
def print_sleep(t):
    print("sleeping for " + str(t))

with patch('time.sleep') as mock_sleep:
    mock_sleep.side_effect = print_sleep 
    wait_n_seconds(1000)

# %% [markdown]
# **Exercise**: Patch the `record_data()` function using a side effect so that, instead of calling `np.savetxt`, the function calls a new function `print_data()` that just prints out what data you stored and where you stored it.
#
# (Hint: since `np.savetxt` is imported into the current namespace you have to call it as `"__main__.np.savetxt"`)
#

# %%
import numpy as np
def record_data():
    np.savetxt('mydata1.txt', [1, 2, 3])
    


# %%

# %% [markdown]
# **Exercise**: Patch the `wait_key()` function using a side effect so that, instead of calling `waitKeys()`, the function calls a new function `return_key()` that just returns the key from the `keyList` passed to `waitKeys()` without waiting. Use the mock to `assert wait_key("a") == "a"`.
#
# (Hint: since `np.savetxt` is imported into the current namespace you have to call it as `"__main__.waitKeys"`)

# %%
from psychopy.event import waitKeys

def wait_key(keyList=["space"]):
    key = waitKeys(keyList=keyList)[0]
    return key


# %%

# %% [markdown]
# BONUS: Mocking Encrytption for Logins
#
# Below is the function login(), which takes in a username and a password and uses a hash algorithm to transform those data to a secure format. Then, the .hexdigest() method transforms the encrypted password int a readable string of letters ready to be sent off to a website.
#
# This way, we can login to a website and even if our transfer is intercepted, our password can not be decrypted. This is great, but it poses a challenge to testing: how can the code that reads out the hash know whether it is valid?
#
# To solve this problem, use patch to:
# - patch the hashlib.sha256 function as hasher
# - inside the patch context, create a Mock object called hash
# - give the hash mock a hexdigest attribute with a return_value
# - use the hash mock as return value of the hasher that patches hashlib.sha256
#
# Then:
# - assert that, when the mock has the return value 'dd130a', login() returns 'logged in.'
# - assert that, when the mock has a different return value, login() returns 'invalid credentials.'
#

# %%
import hashlib

def login(username: str, password: str):
    hash = hashlib.sha256(username.encode() + password.encode()).hexdigest()
    print(hash)
    is_valid = hash[:6] == 'dd130a'
    if is_valid:
        print('logged in.')
    else:
        print('invalid credentials.')

# %%
