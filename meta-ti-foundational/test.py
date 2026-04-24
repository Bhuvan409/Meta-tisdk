#!/usr/bin/env python3
# This file contains intentional syntax errors and code quality issues for testing

# Error 1: Missing parentheses in print (Python 3)
print "Hello World"

# Error 2: Undefined variable
undefined_var = x + 5

# Error 3: Indentation error
def test_function():
print("Bad indentation")

# Error 4: Missing colon in if statement
if True
    print("Missing colon")

# Error 5: Syntax error in try/except
try:
    risky_operation()
except
    print("Missing exception type")

# Error 6: Mixing tabs and spaces for indentation
def mixed_indentation():
    print("This uses spaces")
    print("This uses tabs")

# Error 7: Unused import
import sys
import os
import json

# Error 8: Bare except clause
try:
    some_operation()
except:
    pass

# Error 9: Comparison to None with == instead of is
if variable == None:
    print("Should use 'is None'")

# Error 10: Using mutable default argument
def bad_default(arg=[]):
    arg.append(1)
    return arg

# Error 11: Missing docstring
def undocumented_function(param):
    return param * 2

# Error 12: Line too long (should be detected by style checkers)
very_long_variable_name = "This is a very long string that exceeds the recommended line length limit of 79 or 88 characters depending on the style guide"

# Error 13: Using global variables
global_var = 10
def modify_global():
    global global_var
    global_var += 1

# Error 14: Inconsistent return statements
def inconsistent_returns(x):
    if x > 0:
        return True
    print("Negative value")
    # Missing return in this branch

# Error 15: Syntax error in class definition
class BadClass
    def __init__(self):
        self.value = 42
