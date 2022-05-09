#include <stdio.h>
#include <Python.h>
/**
 * print_python_list_info - prints python list info
 * @p: PyObject
 * Return: no return
 */
void print_python_list_info(PyObject *p)
{
	int size, i = 0;
	PyObject *item;

	size = Py_SIZE(p);
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", (PyListObject *)p->allocated);

	for (; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
