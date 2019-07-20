# -----------------------------------------------------------------------------
# imports
# -----------------------------------------------------------------------------
from setuptools import setup, find_packages
# -----------------------------------------------------------------------------
# helpers
# -----------------------------------------------------------------------------
with open("README.md", "r") as fh:
    long_description = fh.read()
# -----------------------------------------------------------------------------
# setup
# -----------------------------------------------------------------------------
setup(
    name='space-angel',  
    version='0.1',
    author="Luis Monteiro",
    author_email="monteiro.lcm@gmail.com",
    description="Angel",
    long_description=long_description,
    url="",
    packages=[
        'space_angel',
        'space_angel.kernel',
        'space_angel.angels',
        'space_angel.gates',
        'space_angel.resources'
    ],
    install_requires=[
        'parse',
        'gitpython'

    ],
    classifiers=[],
 )
 # ----------------------------------------------------------------------------
 # end
 # ----------------------------------------------------------------------------
