#include "Python.h"
#include <stdio.h>

void print_its2(PyObject *p)
{
    Py_ssize_t length = PyList_GET_SIZE(p);
    Py_ssize_t count = 0;
    PyObject *item;

    for (count = 0; count < length; count++)
    {
        item = PyList_GET_ITEM(p, count);
        PyObject_Print(item, stdout, 0);
        printf("\n");
    }
}
