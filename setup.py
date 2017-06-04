#!/usr/bin/env python

from distutils.core import setup
from distutils.extension import Extension

import numpy

try:
  from Cython.Distutils import build_ext
except ImportError:
  use_cython = False
else:
  use_cython = True

cmdclass = {}
ext_modules = []
include_dirs = [numpy.get_include()]

if use_cython:
  ext_modules += [
      Extension("cbfs", ["cbfs.pyx"], include_dirs=include_dirs),
  ]
  cmdclass.update({'build_ext': build_ext})
else:
  ext_modules += [
      Extension("cbfs", ["cbfs.c"], include_dirs=include_dirs),
  ]

setup(
    name='tensorflow_forward_ad',
    packages=['tensorflow_forward_ad'],
    cmdclass=cmdclass,
    ext_modules=ext_modules,
    version='0.1',
    description='TensorFlow forward-mode automatic differentiation',
    author='Mengye Ren',
    author_email='renmengye@gmail.com',
    url='https://github.com/renmengye/tensorflow-forward-ad',
    download_url='https://github.com/renmengye/tensorflow-forward-ad/archive/0.1.tar.gz',
    keywords=['tensorflow', 'automatic', 'differentiation'],
    classifiers=[],
)