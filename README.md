# 🛠️ ws-hash

![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg) 
![License](https://img.shields.io/badge/license-GNU%20GPLv3-green.svg)

A simple hash library implemented in Python, featuring both 256-bit and 512-bit hash functions.

> [!CAUTION]
> THIS LIBRARY IS NOT TESTED FOR BEING SECURE, DO NOT STORE SENSITIVE INFORMATION WITH THIS.

## Features
> What this silly little library is capable of.

- **256-bit Hashing**: Can produce hashes with a bit size of 256.
- **512-bit Hashing**: Can produce hashes with a bit size of 512.

## Installation
> Installing the silly hash Library.

You can install `ws-hash` by installing the package from the python-package-index (pypi). To do this, run the install command below.

```python
pip install ws-hash
```

## Usage
> Importing the silly Library.

To use the ws-hash functions, you can import them as follows:

```python
import ws_hash
```
Hashing Example

Here's how to hash a string using both the 256-bit and 512-bit functions:

```python
# Hash & print the string in ws256 and ws512.
print(ws_hash.ws256("Lorem ipsum, dolor sit amet."))
print(ws_hash.ws512("Lorem ipsum, dolor sit amet."))
```
