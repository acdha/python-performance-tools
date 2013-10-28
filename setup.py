from distribute_setup import use_setuptools
use_setuptools()

from setuptools import setup


setup(
    name='performance_tools',
    version='0.3',
    author='Chris Adams',
    author_email='chris@improbable.org',
    packages=['performance_tools'],
    url='',
    license='See LICENSE.txt',
    description='Utilities for measuring application performance',
    long_description=open('README.rst').read(),
)
