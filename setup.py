#!/usr/bin/env python3

import subprocess

from setuptools import Extension, setup


def pkgconfig(package):
    result = {}
    for token in subprocess.check_output(['pkg-config', '--libs', '--cflags', package]).decode('utf-8').split():
        if token.startswith('-I'):
            result.setdefault('include_dirs', []).append(token[2:])
        elif token.startswith('-L'):
            result.setdefault('library_dirs', []).append(token[2:])
        elif token.startswith('-l'):
            result.setdefault('libraries', []).append(token[2:])
    return result


setup(
    name='libversion',
    version='0.1.0',
    description='Python bindings for libversion',
    author='Dmitry Marakasov',
    author_email='amdmi3@amdmi3.ru',
    url='https://github.com/repology/pylibversion',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: C',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Version Control',
        'Topic :: System :: Archiving :: Packaging',
        'Topic :: System :: Software Distribution',
    ],
    packages=['libversion'],
    ext_modules=[
        Extension(
            'libversion._libversion',
            sources=['src/_libversion.c'],
            **pkgconfig('libversion')
        )
    ],
    test_suite='tests'
)
