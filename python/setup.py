#!/usr/bin/env python

# not sure if this works yet

try:
    from setuptools import setup
except:
    from distutils.core import setup
    
setup(name='remote-relevance-pytest',
      version='0.9',
      description='Proof of concept written in Python to do remote relevance evaulations',
      license="Apache",
      keywords="bigfix ibm iem tem rest",
      author='James Stewart',
      author_email='jgstew',
      url='https://github.com/jgstew/remote-relevance',
      package_dir = {'': 'python'},
      packages=['test_receive_results'],
     )
