from setuptools import setup, find_packages

setup(
    name='bethesda-ini',
    version='0.1.0',
    packages=find_packages(exclude=['docs', 'tests']),
    python_requires='>=3.7',
    install_requires=[]
)
