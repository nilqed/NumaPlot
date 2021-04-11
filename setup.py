# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 00:59:23 2021

@author: kfp
"""

from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

_sdir = '.'
_name = 'numaplot'
_version = '0.1.0'
_description = 'Numerics- and plot server.'
_ldescr = readme()


setup(name = _name,
      version = _version,
      description = _description,
      long_description= _ldescr,
      long_description_content_type = 'text/x-rst',
      classifiers = [
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3.5',
        'Operating System :: POSIX :: Linux',
        'Topic :: Scientific/Engineering :: Mathematics',
      ],
      keywords = 'fricas, jupyter, computer_algebra, numerics, plotting',
      url = 'http://github.com/nilqed/numaplot',
      author = 'Kurt Pagani',
      author_email = 'nilqed@gmail.com',
      license = 'BSD',
      packages = ['numaplot'],
      install_requires = [
          'web.py',
          'requests',
          'py-gnuplot',
      ],
      include_package_data = True,
      zip_safe = False)

