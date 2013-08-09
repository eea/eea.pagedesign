""" Setup.py
"""
import os
from setuptools import setup, find_packages

NAME = 'eea.pagedesign'
PATH = NAME.split('.') + ['version.txt']
VERSION = open(os.path.join(*PATH)).read().strip()

setup(name=NAME,
      version=VERSION,
      description="",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author=('Alec Ghica (Eaudeweb), Alin Voinea (Eaudeweb), '
              'Antonio De Marinis (EEA), European Environment Agency'),
      license='GPL',
      author_email='webadmin@eea.europa.eu',
      url='http://www.eea.europa.eu/data-and-maps',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['eea'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'eea.design',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
