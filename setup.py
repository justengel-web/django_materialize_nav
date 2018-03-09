"""
    setup.py - Setup file to distribute the library

See Also:
    https://github.com/pypa/sampleproject
    https://packaging.python.org/en/latest/distributing.html
    https://pythonhosted.org/an_example_pypi_project/setuptools.html
"""
import os
import glob

from setuptools import setup

import uuid
from pip.req import parse_requirements


def read(fname):
    """Read in a file"""
    with open(os.path.join(os.path.dirname(__file__), fname), "r") as file:
        return file.read()


if __name__ == "__main__":
    # ===== Requirements =====
    try:
        requirements_file = "requirements.txt"
        requirements = [str(ir.req)
                        for ir in parse_requirements(requirements_file, session=uuid.uuid1())
                        if ir.req is not None]
    except FileNotFoundError:
        requirements = []
    # ===== END Requirements =====

    setup(
        name="django_materialize_nav",
        version="0.1.2",
        description="Django materialize css support with some helpful navigation tools.",
        url="https://github.com/HashSplat/django_materialize_nav",
        download_url="https://github.com/HashSplat/django_materialize_nav/archive/v0.1.2.tar.gz",

        author="Justin Engel",
        author_email="jengel@sealandaire.com",

        license="",

        platforms="any",
        classifiers=["Programming Language :: Python",
                     "Programming Language :: Python :: 3",
                     "Operating System :: OS Independent"],

        scripts=[],

        long_description=read("README.md"),
        packages=["materialize_nav"],
        install_requires=requirements,

        include_package_data=True,

        # package_data={
        #     'package': ['file.dat']
        # }

        # options to install extra requirements
        # extras_require={
        #     'dev': [],
        #     'test': ['converage'],
        # }

        # Data files outside of packages
        # data_files=[('my_data', ["data/my_data.dat"])],

        # keywords='sample setuptools development'

        # entry_points={
        #     'console_scripts': [
        #         'foo = my_package.some_module:main_func',
        #         'bar = other_module:some_func',
        #     ],
        #     'gui_scripts': [
        #         'baz = my_package_gui:start_func',
        #     ]
        # }
    )
