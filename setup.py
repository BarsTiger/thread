from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="thread",
    version="1.0.0",
    scripts=["thread.py"],
    author="BarsTiger",
    description="Small decorator library for launching threads",
    long_description=long_description,
    py_modules=["thread"],
    license='MIT',
    url='https://github.com/BarsTiger/thread',
    long_description_content_type="text/markdown",
    keywords=["threading", "thread", "decorator", "crossplatform"]
)
