"""Setup up for sample distrobution."""

from setuptools import setup

setup(
    name="codewars",
    description="Problems from CodeWars.com",
    version=0.1,
    author="Marc Fieser",
    author_email="midfies@gmail.com",
    license="MIT",
    package_dir={'': 'src'},
    py_modules=['codewars'],
    install_requires=['ipython'],
    extras_require={
        "test": ['tox', 'pytest', 'pytest-watch', 'pytest-cov']
    },
)
