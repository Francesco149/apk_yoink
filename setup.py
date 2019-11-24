#!/bin/env python3

from setuptools import setup, find_packages

apk_yoink_classifiers = [
    "Programming Language :: Python :: 3",
    "Intended Audience :: Developers",
    "License :: Public Domain",
    "Topic :: Software Development :: Libraries",
    "Topic :: Utilities"
]

with open("README.rst", "r") as f:
  apk_yoink_readme = f.read()

setup(
    name="apk_yoink",
    version="0.1.0",
    author="Franc[e]sco",
    author_email="lolisamurai@tfwno.gf",
    url="https://github.com/Francesco149/apk_yoink",
    scripts=["bin/apk-yoink"],
    description=(
        "download android apks from the terminal "
        + "(including region locked ones)"
    ),
    long_description=apk_yoink_readme,
    license="Unlicense",
    classifiers=apk_yoink_classifiers,
    keywords="android apk downloader region lock",
    install_requires=["gachanator", "tqdm"]
)
