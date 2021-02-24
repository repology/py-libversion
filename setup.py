#!/usr/bin/env python3

import shlex
import subprocess
import sys
from os import path

from setuptools import Extension, setup


here = path.abspath(path.dirname(__file__))


def pkgconfig(package):
    result = {}
    pkg_config_output = subprocess.check_output(['pkg-config', '--libs', '--cflags', package]).decode('utf-8')
    for token in shlex.split(pkg_config_output):
        if token.startswith('-I'):
            result.setdefault('include_dirs', []).append(token[2:])
        elif token.startswith('-L'):
            result.setdefault('library_dirs', []).append(token[2:])
        elif token.startswith('-l'):
            result.setdefault('libraries', []).append(token[2:])
    return result


def pkgconfig_libversion():
    try:
        return pkgconfig('libversion')
    except subprocess.CalledProcessError:
        print('MISSING DEPENDENCY: libversion library not found, please install it to continue', file=sys.stderr)
        print('\nSee https://github.com/repology/libversion#building for installation', file=sys.stderr)
        print('instructions', file=sys.stderr)
        sys.exit(1)
    except FileNotFoundError:
        print('MISSING DEPENDENCY: pkg-config not found, please install it to continue', file=sys.stderr)
        print('\nSee https://www.freedesktop.org/wiki/Software/pkg-config/ for installation', file=sys.stderr)
        print('instructions, or install it from your package manager', file=sys.stderr)
        sys.exit(1)


def get_version():
    with open(path.join(here, 'libversion', '__init__.py')) as source:
        for line in source:
            if line.startswith('__version__'):
                return line.strip().split(' = ')[-1].strip("'")

    raise RuntimeError('Cannot determine package version from package source')


def get_long_description():
    try:
        return open(path.join(here, 'README.md')).read()
    except:
        return None


setup(
    name='libversion',
    version=get_version(),
    description='Python bindings for libversion',
    long_description=get_long_description(),
    long_description_content_type='text/markdown',
    author='Dmitry Marakasov',
    author_email='amdmi3@amdmi3.ru',
    url='https://github.com/repology/py-libversion',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: C',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Version Control',
        'Topic :: System :: Archiving :: Packaging',
        'Topic :: System :: Software Distribution',
    ],
    packages=['libversion'],
    package_data={'libversion': ['py.typed', '_libversion.pyi']},
    ext_modules=[
        Extension(
            'libversion._libversion',
            sources=['src/_libversion.c'],
            **pkgconfig_libversion()
        )
    ],
    test_suite='tests'
)
