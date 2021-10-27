from setuptools import setup, find_packages

with open("requirements.txt","r") as f:
    requirements = f.readlines()
setup(
    name='customaugmentator',
    version='1.1',
    packages=find_packages(),
    requirements=requirements,
)
