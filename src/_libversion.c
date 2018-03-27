/*
 * Copyright (c) 2017-2018 Dmitry Marakasov <amdmi3@amdmi3.ru>
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 */

#include <Python.h>
#include <libversion/version.h>

static PyObject* version_compare(PyObject *self, PyObject *args) {
	(void)self; // (unused)

	const char *v1;
	const char *v2;
	int flags1 = 0;
	int flags2 = 0;

	if (!PyArg_ParseTuple(args, "ss|ii", &v1, &v2, &flags1, &flags2))
		return NULL;

	return PyLong_FromLong(version_compare_flags2(v1, v2, flags1, flags2));
}

static PyMethodDef module_methods[] = {
	{"version_compare", (PyCFunction)version_compare, METH_VARARGS, ""},
	{NULL, NULL, 0, NULL}
};

static struct PyModuleDef module_definition = {
	PyModuleDef_HEAD_INIT,
	"_libversion",
	NULL,
	-1,
	module_methods,
	NULL,
	NULL,
	NULL,
	NULL
};

PyMODINIT_FUNC PyInit__libversion(void) {
	PyObject* m = PyModule_Create(&module_definition);

	if (m == NULL)
		return NULL;

	PyModule_AddIntConstant(m, "P_IS_PATCH", VERSIONFLAG_P_IS_PATCH);
	PyModule_AddIntConstant(m, "ANY_IS_PATCH", VERSIONFLAG_ANY_IS_PATCH);

	return m;
}
