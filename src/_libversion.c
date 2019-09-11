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

#if defined(LIBVERSION_VERSION_ATLEAST)
# if LIBVERSION_VERSION_ATLEAST(2, 7, 0)
#  define HAS_VERSION_COMPARE2 1
#  define HAS_VERSION_COMPARE4 1
# endif
#endif

#if defined(LIBVERSION_VERSION_ATLEAST)
# if LIBVERSION_VERSION_ATLEAST(3, 0, 0)
#  define HAS_VERSION_BOUNDS 1
# endif
#endif

static PyObject* py_version_compare2(PyObject *self, PyObject *args) {
	(void)self; // (unused)

	const char *v1;
	const char *v2;

	if (!PyArg_ParseTuple(args, "ss", &v1, &v2))
		return NULL;

	return PyLong_FromLong(
#ifdef HAS_VERSION_COMPARE2
		version_compare2(v1, v2)
#else
		version_compare_simple(v1, v2)
#endif
	);
}

static PyObject* py_version_compare4(PyObject *self, PyObject *args) {
	(void)self; // (unused)

	const char *v1;
	const char *v2;
	int flags1;
	int flags2;

	if (!PyArg_ParseTuple(args, "ssii", &v1, &v2, &flags1, &flags2))
		return NULL;

	return PyLong_FromLong(
#ifdef HAS_VERSION_COMPARE4
		version_compare4(v1, v2, flags1, flags2)
#else
		version_compare_flags2(v1, v2, flags1, flags2)
#endif
	);
}

static PyObject* py_version_compare(PyObject *self, PyObject *args) {
	(void)self; // (unused)

	const char *v1;
	const char *v2;
	int flags1 = 0;
	int flags2 = 0;

	if (!PyArg_ParseTuple(args, "ss|ii", &v1, &v2, &flags1, &flags2))
		return NULL;

	return PyLong_FromLong(
#ifdef HAS_VERSION_COMPARE4
		version_compare4(v1, v2, flags1, flags2)
#else
		version_compare_flags2(v1, v2, flags1, flags2)
#endif
	);
}

static PyMethodDef module_methods[] = {
	{"version_compare2", (PyCFunction)py_version_compare2, METH_VARARGS, ""},
	{"version_compare4", (PyCFunction)py_version_compare4, METH_VARARGS, ""},
	{"version_compare", (PyCFunction)py_version_compare, METH_VARARGS, ""},
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

#ifdef HAS_VERSION_BOUNDS
	PyModule_AddIntConstant(m, "LOWER_BOUND", VERSIONFLAG_LOWER_BOUND);
	PyModule_AddIntConstant(m, "UPPER_BOUND", VERSIONFLAG_UPPER_BOUND);
#else
	// stub
	PyModule_AddIntConstant(m, "LOWER_BOUND", 0);
	PyModule_AddIntConstant(m, "UPPER_BOUND", 0);
#endif

	return m;
}
