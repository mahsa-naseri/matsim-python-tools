import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="matsim_tools",
    version="0.0.1",
    description="Tools for working with the MATSim Agent-Based Transportation Simulation framework",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/matsim-vsp/matsim-python-tools",
    author="VSP-Berlin",
    author_email="laudan@tu-berlin.de",
    license="GPL-3",
    classifiers=[
        "License :: OSI Approved :: GPL License",
        "Programming Language :: Python :: 3",
    ],
    packages=["matsim_tools"],
    install_requires=[],
    entry_points={},
)