#!/usr/bin/env python

from setuptools import setup
import os

install_requires = [
	"argparse"
    ]

test_requires = [
    ]

data_files=[]


with open("README.md", "r") as fh:
	long_description = fh.read()

here = os.path.abspath(os.path.dirname(__file__))
about = {}
with open(os.path.join(here, "basically_ti_basic", "__version__.py"), "r") as f:
	exec(f.read(), about)


setup(name=about["__title__"],
    version=about["__version__"],
    description=about["__description__"],
    author=about["__author__"],
    author_email=about["__author_email__"],
    url=about["__url__"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=install_requires,
    tests_require=test_requires,
    entry_points={
        'console_scripts': [
            'basically-ti-basic = basically_ti_basic.main:main',
            'tibc = basically_ti_basic.main:main'
        ]
    },
    test_suite='nose.collector',
    packages=[
        'basically_ti_basic',
        'basically_ti_basic.compiler',
        'basically_ti_basic.files',
        'basically_ti_basic.tokens'
        ],
	classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
	python_requires='>=3.6',
    data_files=data_files,
    package_data={
        }
    )
