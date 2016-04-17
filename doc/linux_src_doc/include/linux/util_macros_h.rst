.. -*- coding: utf-8; mode: rst -*-

=============
util_macros.h
=============


.. _`find_closest`:

find_closest
============

.. c:function:: find_closest ( x,  a,  as)

    locate the closest element in a sorted array

    :param x:
        The reference value.

    :param a:
        The array in which to look for the closest element. Must be sorted
        in ascending order.

    :param as:
        Size of 'a'.



.. _`find_closest.description`:

Description
-----------

Returns the index of the element closest to 'x'.



.. _`find_closest_descending`:

find_closest_descending
=======================

.. c:function:: find_closest_descending ( x,  a,  as)

    locate the closest element in a sorted array

    :param x:
        The reference value.

    :param a:
        The array in which to look for the closest element. Must be sorted
        in descending order.

    :param as:
        Size of 'a'.



.. _`find_closest_descending.description`:

Description
-----------

Similar to :c:func:`find_closest` but 'a' is expected to be sorted in descending
order.

