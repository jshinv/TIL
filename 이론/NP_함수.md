# NP_함수



##### Parameters

- **shape** : tuple of ints

  Shape of created array.

- **dtype** : data-type, optional

  Any object that can be interpreted as a numpy data type.

- **buffer** : object exposing buffer interface, optional

  Used to fill the array with data.

- **offset** : int, optional

  Offset of array data in buffer.

- **strides** : tuple of ints, optional

  Strides of data in memory.

- **order** : {‘C’, ‘F’}, optional

  Row-major (C-style) or column-major (Fortran-style) order.



	> See also
	>
	> - [`array`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.array.html#numpy.array)
	>
	>   Construct an array.
	>
	> - [`zeros`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.zeros.html#numpy.zeros)
	>
	>   Create an array, each element of which is zero.
	>
	> - [`empty`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.empty.html#numpy.empty)
	>
	>   Create an array, but leave its allocated memory unchanged (i.e., it contains “garbage”).
	>
	> - [`dtype`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.dtype.html#numpy.dtype)
	>
	>   Create a data-type.



---



##### Attributes

[`T`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.T.html#numpy.ndarray.T) : ndarray

The transposed array.

[`data`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.data.html#numpy.ndarray.data) : buffer

Python buffer object pointing to the start of the array’s data.

[`dtype`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.dtype.html#numpy.dtype) : dtype object

Data-type of the array’s elements.

[`flags`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.flags.html#numpy.ndarray.flags) : dict

Information about the memory layout of the array.

[`flat`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.flat.html#numpy.ndarray.flat) : numpy.flatiter object

A 1-D iterator over the array.

[`imag`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.imag.html#numpy.imag) : ndarray

The imaginary part of the array.

[`real`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.real.html#numpy.real) : ndarray

The real part of the array.

[`size`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.size.html#numpy.ndarray.size) : int

Number of elements in the array.

[`itemsize`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.itemsize.html#numpy.ndarray.itemsize) : int

Length of one array element in bytes.

[`nbytes`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.nbytes.html#numpy.ndarray.nbytes) : int

Total bytes consumed by the elements of the array.

[`ndim`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.ndim.html#numpy.ndarray.ndim) : int

Number of array dimensions.

[`shape`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.shape.html#numpy.ndarray.shape) : tuple of ints

Tuple of array dimensions.

[`strides`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.strides.html#numpy.ndarray.strides) : tuple of ints

Tuple of bytes to step in each dimension when traversing an array.

[`ctypes`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.ctypes.html#numpy.ndarray.ctypes) : ctypes object

An object to simplify the interaction of the array with the ctypes module.

[`base`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.base.html#numpy.ndarray.base) : ndarray

Base object if memory is from some other object.



---



##### Methods

URL : https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.html



---

참고 URL : https://pandas.pydata.org/pandas-docs/stable/reference/series.html