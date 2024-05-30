#!/usr/bin/env python

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="audo-dataset-encoder",
    version="1.0.0",
    author="dmforit",
    author_email="edudkaratyshchev@gmail.com",
    description="Make your preprocessing stage automated!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='Apache License 2.0',
    url="https://github.com/dmforit/auto-dataset-encoder",
    packages=setuptools.find_packages(exclude=("tests",)),
    install_requires=[
        "category-encoders==2.6.3",
        "joblib>=1.4.2",
        "numpy>=1.26.4",
        "packaging==24.0",
        "pandas>=2.2.2",
        "patsy>=0.5.6",
        "python-dateutil>=2.9.0.post0",
        "pytz>=2024.1",
        "scikit-learn>=1.5.0",
        "scipy>=1.13.1",
        "six==1.16.0",
        "statsmodels>=0.14.2",
        "threadpoolctl>=3.5.0",
        "tzdata>=2024.1"
        
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)