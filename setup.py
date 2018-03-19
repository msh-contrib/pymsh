import io
import os
import re
import sys

from setuptools import setup


def get_variable(var_name):
    regex = "__{var_name}__\s=\s\'(?P<{var_name}>.*)\'".format(
        var_name=var_name)

    path = ('msh', '__init__.py',)

    return re.search(regex, read(*path)).group(var_name)


def read(*parts):
    filename = os.path.join(os.path.abspath(os.path.dirname(__file__)), *parts)

    sys.stdout.write(filename)

    with io.open(filename, encoding='utf-8', mode='rt') as fp:
        return fp.read()


packages = ['msh']


install_requires = []


classifiers = ['Intended Audience :: Developers',
               'License :: OSI Approved :: MIT License',
               'Programming Language :: Python',
               'Programming Language :: Python :: 3.6',
               ]

setup(
    name='msh',
    version=get_variable('version'),
    description=get_variable('description'),
    long_description=read('README.md'),
    url='https://github.com/msh-contrib/msh',
    author='Oleh Kuchuk',
    author_email='kuchuklehjs@gmail.com',
    license=read('LICENSE.txt'),
    packages=packages,
    install_requires=install_requires,
    zip_safe=False,
    classifiers=classifiers,
    entry_points={
        'console_scripts': [
            'msh=msh.cli:entrypoint'
        ],
    },
    keywords=[
        'shell',
        'posix',
        'bash',
    ],
)
