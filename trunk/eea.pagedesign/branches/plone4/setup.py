""" Setup.py
"""
import os
from os.path import join
from setuptools import setup, find_packages

name = 'eea.pagedesign'
path = name.split('.') + ['version.txt']
version = open(join(*path)).read().strip()

setup(name='eea.pagedesign',
      version=version,
      description="",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='',
      author_email='',
      url='',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['eea'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'eea.design',
          'eea.testcase'
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
