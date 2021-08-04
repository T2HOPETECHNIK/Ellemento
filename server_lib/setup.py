from setuptools import setup

setup(
    name='ellemento',
    version='0.0.1',
    packages=['ellemento'],
    install_requires=[
        'requests',
        'importlib; python_version == "3.7.4"',
    ],
)