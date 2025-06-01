=====
Numpy
=====

While Python's built-in data structures e.g. ``list``, are powerful and flexible, 
sometimes you need even more - especially when working with large datasets or doing 
scientific and numerical computing.

.. image:: /_static/images/python_day_01/slow.jpg
   :alt: Python is fast
   :align: center
   :width: 400px


**NumPy** is a popular external library that introduces the array data structure, which 
looks and feels a lot like a Python list but offers better performance with the right
mathematical implementation.

------------
Installation
------------

``pip`` comes in default with python as the package manager to install and manage packages 
from `PyPI <https://pypi.org/>`_. To install ``numpy``

.. code-block:: shell

    pip install numpy

-------
Example
-------

Let's say you have a grayscale image stored as a 2D NumPy array, with pixel values between 
0 and 1. Even though the pixel values are between 0 and 1, the average brightness can still 
vary from image to image. One image might be mostly dark, another might be very bright. This 
variation can affect how well a model learns, since it might pick up on brightness differences 
instead of actual shapes or patterns. 

By applying Z-score normalization, we shift the data so its mean becomes 0 and its spread becomes consistent.
This removes brightness bias and makes the data more stable and reliable for learning.

.. math::

    \text{normalized} = \frac{x - \text{mean}}{\text{std}}


.. literalinclude:: scripts/numpy_example.py
   :language: python
   :linenos:
