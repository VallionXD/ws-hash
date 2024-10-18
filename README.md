# 🛠️ ws-hash

![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg) 
![License](https://img.shields.io/badge/license-GNU%20GPLv3-green.svg)

A simple yet hash library implemented in Python, featuring both 256-bit and 512-bit hash functions.

**DISCLAIMER**: THIS LIBRARY IS NOT TESTED FOR BEING SECURE, DO NOT STORE SENSITIVE INFORMATION WITH THIS.

## Features
> What this silly little library is capable of.

- **256-bit Hashing**: Can produce hashes with a bit size of 256.
- **512-bit Hashing**: Can produce hashes with a bit size of 512.

## Installation
> Installing the silly hash Library.

You can install `ws-hash` by downloading the python file. You can download it from the source view, and place it into your python project folder / directory.

## Usage
> Importing the silly Library.

To use the ws-hash functions, you can import them as follows:

```python
# Import both functions from the ws-hash file.
from ws-hash import ws256, ws512
```
Hashing Example

Here's how to hash a string using both the 256-bit and 512-bit functions:

```python
# Hash & print the string in ws256 and ws512.
print(ws256("Lorem ipsum, dolor sit amet."))
print(ws512("Lorem ipsum, dolor sit amet."))
```
