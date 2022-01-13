from importlib.metadata import entry_points
from setuptools import setup, find_packages

setup (
    name="gitbees",
    version="0.1.0",
    author="Marcello Belanda",
    packages=find_packages(),
    entry_points="""
    [console_scripts]
    gitbees=gitbees:main
    """
)