"""
1. functions in Python.
What you need to know about functions in Python for decorators.
"""


"""
In python, functions are objects, therefore they can be used in many ways:

1.1 functions can be assigned to variables.
"""


def assignable_functions():
    print('hello world')


print('1.1 functions can be assigned to variables.')
hello_world_function = assignable_functions
hello_world_function()


"""
1.2 can define inner functions
"""


def outer_function(name):

    def get_hi():
        return 'hi'

    return get_hi() + ' ' + name


print('1.2 can define inner functions')
print(outer_function('Seattle'))


"""
1.3 functions can return functions
"""


def get_hello_world_function():

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
    return string.capitalize()


def get_formatted_string(formatter, string):
    return formatter(string)


print('1.4 functions can be parameters.')

print(get_formatted_string(capitalize, "proudly cap'ed"))


"""
1.5 inner function can access outer scope (closure)
"""


def old_outer_function(name):

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

    def inner_scope_function():
        capped_name = name.capitalize()
        # name = 'some other name'
        return 'Hello ' + name

    return inner_scope_function


print('1.5.1 Note: inner function cannot assign to outer scope')

kitty_function = outer_scope_function('Kitty')
print(kitty_function())
