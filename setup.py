from setuptools import setup, find_packages
import sys, os

version = '1.0'

setup(name='fanstatictemplate',
      version=version,
      description="Fanstatic package template",
      author='Fanstatic Developers',
      author_email='fanstatic@googlegroups.com',
      url='http://fanstatic.org',
      license='BSD',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'PasteScript',
      ],
      extras_require=['pytest'],
      entry_points={
          'paste.paster_create_template':
              ['fanstatic = fanstatictemplate:Template']},
      )
