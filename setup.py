
import sys

from setuptools import setup, find_packages

extra_setup = {}
if sys.version_info >= (3,):
    extra_setup['use_2to3'] = True

setup(
    name='nosenicedots',
    version='0.1',
    description="",
    long_description="""""",
    author='Kumar McMillan',
    author_email='kumar.mcmillan@gmail.com',
    license="Apache License",
    packages=find_packages(exclude=['ez_setup']),
    install_requires=[r for r in open('requirements.txt')
                      if r.strip() and not r.startswith('#')],
    url='',
    include_package_data=True,
    entry_points="""
        [nose.plugins.0.10]
        nicedots = nosenicedots:NiceDots
        """,
    classifiers = [
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Testing'
        ],
    **extra_setup
    )
