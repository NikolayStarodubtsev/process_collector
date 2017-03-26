from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='process_collector',

    version='0.0.1',

    description='Python script which can collect running processes',
    long_description=long_description,

    url='https://github.com/NikolayStarodubtsev/process_collector',

    author='Nikolai Starodubtcev',
    author_email='starodubcevna@gmail.com',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='process monitor',

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    install_requires=['psutil'],

    entry_points={
        'console_scripts': [
            'process_collector = process_collector.__main__:main',
        ],
    },
)
