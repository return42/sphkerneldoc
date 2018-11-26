.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/util_macros.h

.. _`find_closest`:

find_closest
============

.. c:function::  find_closest( x,  a,  as)

    locate the closest element in a sorted array

    :param x:
        The reference value.
    :type x: 

    :param a:
        The array in which to look for the closest element. Must be sorted
        in ascending order.
    :type a: 

    :param as:
        Size of 'a'.
    :type as: 

.. _`find_closest.description`:

Description
-----------

Returns the index of the element closest to 'x'.

.. _`find_closest_descending`:

find_closest_descending
=======================

.. c:function::  find_closest_descending( x,  a,  as)

    locate the closest element in a sorted array

    :param x:
        The reference value.
    :type x: 

    :param a:
        The array in which to look for the closest element. Must be sorted
        in descending order.
    :type a: 

    :param as:
        Size of 'a'.
    :type as: 

.. _`find_closest_descending.description`:

Description
-----------

Similar to \ :c:func:`find_closest`\  but 'a' is expected to be sorted in descending
order.

.. This file was automatic generated / don't edit.

