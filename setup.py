#!/usr/bin/env python
import os
import shutil
import sys
from codecs import open

from setuptools import setup

CURRENT_PYTHON = sys.version_info[:2]
REQUIRED_PYTHON = (3, 8)

if CURRENT_PYTHON < REQUIRED_PYTHON:
    sys.stderr.write(
        f"Unsupported Python version - requires at least "
        f"{REQUIRED_PYTHON[0]}.{REQUIRED_PYTHON[1]}"
    )
    sys.exit(1)

# 'setup.py publish' shortcut.
if sys.argv[-1] == "publish":
    shutil.rmtree("build")
    shutil.rmtree("dist")
    os.system("python setup.py sdist bdist_wheel")
    os.system("twine upload dist/*")
    sys.exit()

requires: list[str] = []

here = os.path.abspath(os.path.dirname(__file__))

with open("README.md", "r", "utf-8") as f:
    readme = f.read()

setup(
    name="konso_dice_roller",
    version="0.0.6",
    description="A simple dice roller library",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Tomi Javanainen",
    author_email="tomi.javanainen@gmail.com",
    url="https://github.com/konsou/konso_dice_roller",
    packages=["konso_dice_roller"],
    package_data={"": ["LICENSE"]},
    package_dir={"konso_dice_roller": "konso_dice_roller"},
    include_package_data=True,
    python_requires=">=3.8, <4",
    install_requires=requires,
    license="MIT",
    zip_safe=False,
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: Finnish",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Software Development :: Libraries",
    ],
    project_urls={
        "Source": "https://github.com/konsou/konso_dice_roller",
    },
)
