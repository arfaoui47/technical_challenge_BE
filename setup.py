# This file is part of the technical-challlenge-be project
# https://github.com/technical_challenge_be/technical-challlenge-be
#
# Copyright (c) 2019 Atef Arfaoui (arfatef@gmail.com) - All Rights Reserved
# SPDX-License-Identifier: Proprietary

import os
import setuptools


def project_path(*sub_paths):
    project_dirpath = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(project_dirpath, *sub_paths)


def read(*sub_paths):
    with open(project_path(*sub_paths), mode="rb") as fh:
        return fh.read().decode("utf-8")


install_requires = [
    line.strip()
    for line in read("requirements", "pypi.txt").splitlines()
    if line.strip() and not line.startswith("#")
]


long_description = "\n\n".join((read("README.md"), read("CHANGELOG.md")))


setuptools.setup(
    name="technical-challlenge-be",
    license="Copyright (c) 2019 Atef Arfaoui (arfatef@gmail.com) - All Rights Reserved",
    author="Atef Arfaoui",
    author_email="arfatef@gmail.com",
    url="https://github.com/technical_challenge_be/technical-challlenge-be",
    version="201908.1a0",
    keywords="Technical challenge for BE",
    description="Example description.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages("src/"),
    package_dir={"": "src"},
    install_requires=install_requires,
    entry_points="""
        [console_scripts]
        technical_challlenge_be=technical_challlenge_be.__main__:cli
    """,
    python_requires=">=3.6",
    zip_safe=True,

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "License :: Other/Proprietary License",
        "Operating System :: Unix",
        "Operating System :: POSIX",
        "Operating System :: MacOS :: MacOS X",
        # "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
