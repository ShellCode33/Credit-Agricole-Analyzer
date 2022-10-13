#!/usr/bin/python3
# coding: utf-8

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='credit-agricole-analyzer',
    version='0.1',
    description='Analyze your Credit Agricole bank account to give you valuable insights',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords="credit agricole bank account card loan insurance",
    license="MIT",
    author='ShellCode',
    author_email='shellcode33@protonmail.ch',
    url='https://github.com/ShellCode33/Credit-Agricole-Analyzer',
    packages=find_packages(),
    python_requires='>=3.6',

    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        'License :: OSI Approved :: MIT License',
        "Operating System :: POSIX :: Linux",
    ],

    install_requires=[
        "credit-agricole",
        "pandas",
        "ipython",
        "matplotlib",
        "mplcursors",
    ],

    entry_points={
        "console_scripts": [
            "ca-analyzer = ca_analyzer.frontends.cli:main",
        ]
    }
)
