#!/usr/bin/python3
"""Write Our C code,
Complie it into a library
Use a C library in python,
Read the C library,
Use library Functions
Using library objects, like Lists and Dictionaries"""

"""gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -o libmy.so -fPIC -I/usr/include/python3.9  *.c"""
"""gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,PyList -o libmy.so -fPIC -I/usr/include/python3.4 *.c"""

import ctypes
my_lib = ctypes.PyDLL("./libmy.so")

"""
my_lib.print_its.argtypes = [ctypes.c_char_p]
my_lib.print_its.restypes = ctypes.c_int

num = my_lib.print_its(b"What is happening\n")
print(num)

my_lib.greetings()

add_func = my_lib.add_it
add_func.argtypes = [ctypes.c_int, ctypes.c_int]
add_func.restypes = ctypes.c_int

res = add_func(20, 45)
print(res)
"""

my_lib.print_its2.argtypes = [ctypes.py_object]
my_lib.print_its2([4, 2, 7, 7, 9])
