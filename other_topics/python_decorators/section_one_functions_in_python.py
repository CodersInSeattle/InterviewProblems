# pylint: disable=pointless-string-statement, missing-docstring, invalid-name

"""
1. functions in Python.
What you need to know about functions in Python for decorators.
"""


"""
In python, functions are first class citizens; they can be used in many ways.
https://en.wikipedia.org/wiki/First-class_function

1.1 functions can be assigned to variables.
"""


def assignable_functions():
    """ Prints hello world"""
    print('hello world')


print('1.1 functions can be assigned to variables.')
hello_world_function = assignable_functions
hello_world_function()


"""
1.2 functions can define inner functions
"""


def outer_function(name):
    """ A function that defines an inner function and use it. """

    def get_hi():
        return 'hi'

    return get_hi() + ' ' + name


print('1.2 functions can define inner functions')
print(outer_function('Seattle'))


"""
1.3 functions can return functions
"""


def get_hello_world_function():
    """
    A function that returns a function.
    """
    def inner_hello_world_function():
        return 'hello world again, this is not fun.'

    return inner_hello_world_function


print('1.3 functions can return functions')

my_inner_hello_world_function = get_hello_world_function()
print(my_inner_hello_world_function)
print(my_inner_hello_world_function())


"""
1.4 functions can be parameters.
"""


def capitalize(string):
    """
    Given a str string, returns a string with all characters in string
    capitalized.
    :param string: a string
    :return: capitalized string
    """
    return string.capitalize()


def get_formatted_string(formatter, string):
    """
    Given a string formatter `formatter` and a str `string`, returns the result
    of the formatter applied to  the string.
    :param formatter: the formatter function which take a str as a parameter
    :param string: a str
    :return: the formatted string
    """
    return formatter(string)


print('1.4 functions can be parameters.')

print(get_formatted_string(capitalize, "proudly cap'ed"))


"""
1.5 inner function can access outer scope (closure)
"""


def old_outer_function(name):
    """
    Given a str name, returns a function that will return 'Hello `name`' when
     called.
    :param name: a str
    :return: a function.
    """

    def new_inner_function():
        return 'Hello ' + name

    return new_inner_function


print('1.5 inner function can access outer scope (closure)')

hello_name_function = old_outer_function('42')
print(hello_name_function())


"""
1.5.1 Note: inner function cannot assign to outer scope
"""


def outer_scope_function(name):
    """
    Given a str name, returns a function that will return 'Hello `name`' when
     called.
    :param name: a str
    :return: a function.
    """

    def inner_scope_function():
        _ = name.capitalize()
        # uncomment the following line and you will have an error. Python does
        #  not make its scope dynamically.
        # name = 'some other name'
        return 'Hello ' + name

    return inner_scope_function


print('1.5.1 Note: inner function cannot assign to outer scope')

kitty_function = outer_scope_function('Kitty')
print(kitty_function())
