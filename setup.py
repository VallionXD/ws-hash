# setup.py
from setuptools import setup, find_packages

setup(
    name='ws_hash',
    version='1.1.0',
    packages=find_packages(),
    description='A simple hash library implemented in Python, featuring both 256-bit and 512-bit hash functions.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='VallionXD',
    author_email='',
    url='https://github.com/VallionXD/ws-hash/',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
