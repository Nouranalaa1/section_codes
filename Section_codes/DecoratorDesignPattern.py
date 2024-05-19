"""
Decorator Basics
"""
#Python’s functions are objects

def shout(word='yes'):
    return word.capitalize() + '!'

print (shout())
# outputs : 'Yes!'

# As an object, you can assign the function to a variable like any
# other object 

scream = shout

# Notice we don’t use parentheses: we are not calling the function, we are
# putting the function `shout` into the variable `scream`. 
# It means you can then call `shout` from `scream`:

print (scream())
# outputs : 'Yes!'

# More than that, it means you can remove the old name `shout`, and
# the function will still be accessible from `scream`

del shout
try:
    print (shout())
except NameError as e:
    print (e)
    #outputs: "name 'shout' is not defined"

print (scream())
# outputs: 'Yes!'

def talk():
    # You can define a function on the fly in `talk` ...
    def whisper(word='yes'):
        return word.lower() + '...'

    # ... and use it right away!
    print(whisper())

# You call `talk`, that defines `whisper` EVERY TIME you call it, then
# `whisper` is called in `talk`. 
talk()
# outputs: 
# "yes..."

# But `whisper` DOES NOT EXIST outside `talk`:
try:
    print(whisper())
except NameError as e:
    print(e)  # outputs: "name 'whisper' is not defined"

# Explanation:
# Python's functions are objects, so `whisper` is defined every time `talk` is called.
# Outside the `talk` function, `whisper` is not defined and will raise a NameError.
"""
Functions references
"""
def getTalk(kind='shout'):

    # We define functions on the fly
    def shout(word='yes'):
        return word.capitalize() + '!'

    def whisper(word='yes'):
        return word.lower() + '...'

    # Then we return one of them
    if kind == 'shout':
        # We don’t use '()'. We are not calling the function;
        # instead, we’re returning the function object
        return shout  
    else:
        return whisper

# How do you use this strange beast?

# Get the function and assign it to a variable
talk = getTalk()      

# You can see that `talk` is here a function object:
print(talk)
#outputs : <function getTalk.<locals>.shout at 0x...>

# The object is the one returned by the function:
print(talk())
#outputs : Yes!

# And you can even use it directly if you feel wild:
print(getTalk('whisper')())
#outputs : yes...

def doSomethingBefore(func): 
    print('I do something before then I call the function you gave me')
    print(func())

def scream():
    return 'Aaaah!'

doSomethingBefore(scream)
# outputs: 
# I do something before then I call the function you gave me
# Aaaah!

"""
Handcrafted decorators
"""
# A decorator is a function that expects ANOTHER function as parameter
def my_shiny_new_decorator(a_function_to_decorate):

    # Inside, the decorator defines a function on the fly: the wrapper.
    # This function is going to be wrapped around the original function
    # so it can execute code before and after it.
    def the_wrapper_around_the_original_function():
        
        # Put here the code you want to be executed BEFORE the original 
        # function is called
        print('Before the function runs')

        # Call the function here (using parentheses)
        a_function_to_decorate()

        # Put here the code you want to be executed AFTER the original 
        # function is called
        print('After the function runs')

    # At this point, `a_function_to_decorate` HAS NEVER BEEN EXECUTED.
    # We return the wrapper function we have just created.
    # The wrapper contains the function and the code to execute before
    # and after. It’s ready to use!
    return the_wrapper_around_the_original_function

# Now imagine you create a function you don’t want to ever touch again.
def a_stand_alone_function():
    print('I am a stand alone function, don’t you dare modify me')

a_stand_alone_function() 
# outputs: I am a stand alone function, don’t you dare modify me

# Well, you can decorate it to extend its behavior.
# Just pass it to the decorator, it will wrap it dynamically in 
# any code you want and return you a new function ready to be used:

a_stand_alone_function_decorated = my_shiny_new_decorator(a_stand_alone_function)
a_stand_alone_function_decorated()
# outputs:
# Before the function runs
# I am a stand alone function, don’t you dare modify me
# After the function runs

a_stand_alone_function = my_shiny_new_decorator(a_stand_alone_function)
a_stand_alone_function()
#outputs:
#Before the function runs
#I am a stand alone function, don’t you dare modify me
#After the function runs

# And guess what? That’s EXACTLY what decorators do!

"""
Decorators demystified
"""
@my_shiny_new_decorator
def another_stand_alone_function():
    print ('Leave me alone')

another_stand_alone_function()  
#outputs:  
#Before the function runs
#Leave me alone
#After the function runs
another_stand_alone_function = my_shiny_new_decorator(another_stand_alone_function)

def bread(func):
    def wrapper():
        print("</''''''\>")
        func()
        print("<\______/>")
    return wrapper

def ingredients(func):
    def wrapper():
        print('#tomatoes#')
        func()
        print('~salad~')
    return wrapper

def sandwich(food='--ham--'):
    print(food)

# Direct call to sandwich function
sandwich() 
# outputs: --ham--

# Decorating the sandwich function with bread and ingredients
sandwich = bread(ingredients(sandwich))
sandwich()
# outputs:
# </''''''\>
# #tomatoes#
# --ham--
# ~salad~
# <\______/>
"""
How can the decorators be useful?
"""
import time

def benchmark(func):
    """
    A decorator that prints the time a function takes
    to execute.
    """
    def wrapper(*args, **kwargs):
        t = time.perf_counter()
        res = func(*args, **kwargs)
        print(func.__name__, time.perf_counter() - t)
        return res
    return wrapper


def logging(func):
    """
    A decorator that logs the activity of the script.
    (it actually just prints it, but it could be logging!)
    """
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print(func.__name__, args, kwargs)
        return res
    return wrapper


def counter(func):
    """
    A decorator that counts and prints the number of times a function has been executed
    """
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        res = func(*args, **kwargs)
        print('{0} has been used: {1}x'.format(func.__name__, wrapper.count))
        return res
    wrapper.count = 0
    return wrapper

@counter
@benchmark
@logging
def reverse_string(string):
    return str(reversed(string))

print(reverse_string('Able was I ere I saw Elba'))
print(reverse_string('A man, a plan, a canoe, pasta, heros, rajahs, a coloratura, maps, snipe, percale, macaroni, a gag, a banana bag, a tan, a tag, a banana bag again (or a camel), a crepe, pins, Spam, a rut, a Rolo, cash, a jar, sore hats, a peon, a canal: Panama!'))
################################################################################33

"""Print the runtime of the decorated function"""

import functools
import time

# ...

def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__}() in {run_time:.4f} secs")
        return value
    return wrapper_timer

"""Print the function signature and return value"""
def debug(func):
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]  #create list of args
        kwargs_repr = [f"{k}={repr(v)}" for k, v in kwargs.items()] #create list of kargs
        signature = ", ".join(args_repr + kwargs_repr) #create function signature
        print(f"Calling {func.__name__}({signature})") #print signature
        value = func(*args, **kwargs)
        print(f"{func.__name__}() returned {repr(value)}") #print the return value
        return value
    return wrapper_debug
   
"""Sleep 1 second before calling the function"""

import functools
import time

# ...

def slow_down(func):
    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)
    return wrapper_slow_down