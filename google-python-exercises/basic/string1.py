#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Basic string exercises
# Fill in the code for the functions below. main() is already set up
# to call the functions with a few different inputs,
# printing 'OK' when each function is correct.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.
# It's ok if you do not complete all the functions, and there
# are some additional functions to try in string2.py.


# A. donuts
def donuts(count: int) -> str:
    '''
    Given an int count of a number of donuts, return a string
    of the form 'Number of donuts: <count>', where <count> is the number
    passed in. However, if the count is 10 or more, then use the word 'many'
    instead of the actual count.

    So donuts(5) returns 'Number of donuts: 5'
    and donuts(23) returns 'Number of donuts: many'
    '''
    if count < 10:
        return f"Number of donuts: {count}"

    return "Number of donuts: many"


# B. both_ends´
def both_ends(s: str) -> str:
    '''
    Given a string s, return a string made of the first 2
    and the last 2 chars of the original string,
    so 'spring' yields 'spng'. However, if the string length
    is less than 2, return instead the empty string.
    '''
    if len(s) < 2:
        return ""

    return s[:2] + s[-2:]


# C. fix_start
def fix_start(s: str) -> str:
    '''
    Given a string s, return a string
    where all occurences of its first char have
    been changed to '*', except do not change
    the first char itself.

    e.g. 'babble' yields 'ba**le'
    Assume that the string is length 1 or more.
    Hint: s.replace(stra, strb) returns a version of string s
    where all instances of stra have been replaced by strb.
    '''
    return s[0] + s.replace(s[0], "*", -1)[1:]


# D. MixUp
def mix_up(a: str, b: str) -> str:
    '''
    Given strings a and b, return a single string with a and b separated
    by a space '<a> <b>', except swap the first 2 chars of each string.
    e.g.
      'mix', pod' -> 'pox mid'
      'dog', 'dinner' -> 'dig donner'
    Assume a and b are length 2 or more.
    '''

    # I suspect that here should be a better way to do this without making a
    # new variable perhaps
    new_a = a[0] + b[1:]
    b = b[0] + a[1:]
    return b + " " + new_a


def test(got, expected):
    '''
    Provided simple test() function used in main() to print
    what each function returns vs. what it's supposed to return.
    '''
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '

    print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


def main():
    '''
    Provided main() calls the above functions with interesting inputs,
    using test() to check if each result is correct or not.
    '''
    print('donuts')
    # Each line calls donuts, compares its result to the expected for that call
    test(donuts(4), 'Number of donuts: 4')
    test(donuts(9), 'Number of donuts: 9')
    test(donuts(10), 'Number of donuts: many')
    test(donuts(99), 'Number of donuts: many')

    print()
    print('both_ends')
    test(both_ends('spring'), 'spng')
    test(both_ends('Hello'), 'Helo')
    test(both_ends('a'), '')
    test(both_ends('xyz'), 'xyyz')

    print()
    print('fix_start')
    test(fix_start('babble'), 'ba**le')
    test(fix_start('aardvark'), 'a*rdv*rk')
    test(fix_start('google'), 'goo*le')
    test(fix_start('donut'), 'donut')

    print()
    print('mix_up')
    test(mix_up('mix', 'pod'), 'pox mid')
    test(mix_up('dog', 'dinner'), 'dig donner')
    test(mix_up('gnash', 'sport'), 'spash gnort')
    test(mix_up('pezzy', 'firm'), 'fizzy perm')


# Standard boilerplate to call the main() function.
if __name__ == '__main__':
    main()
