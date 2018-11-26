.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/overflow.h

.. _`array_size`:

array_size
==========

.. c:function:: size_t array_size(size_t a, size_t b)

    Calculate size of 2-dimensional array.

    :param a:
        dimension one
    :type a: size_t

    :param b:
        dimension two
    :type b: size_t

.. _`array_size.description`:

Description
-----------

Calculates size of 2-dimensional array: \ ``a``\  * \ ``b``\ .

.. _`array_size.return`:

Return
------

number of bytes needed to represent the array or SIZE_MAX on
overflow.

.. _`array3_size`:

array3_size
===========

.. c:function:: size_t array3_size(size_t a, size_t b, size_t c)

    Calculate size of 3-dimensional array.

    :param a:
        dimension one
    :type a: size_t

    :param b:
        dimension two
    :type b: size_t

    :param c:
        dimension three
    :type c: size_t

.. _`array3_size.description`:

Description
-----------

Calculates size of 3-dimensional array: \ ``a``\  * \ ``b``\  * \ ``c``\ .

.. _`array3_size.return`:

Return
------

number of bytes needed to represent the array or SIZE_MAX on
overflow.

.. _`struct_size`:

struct_size
===========

.. c:function::  struct_size( p,  member,  n)

    Calculate size of structure with trailing array.

    :param p:
        Pointer to the structure.
    :type p: 

    :param member:
        Name of the array member.
    :type member: 

    :param n:
        Number of elements in the array.
    :type n: 

.. _`struct_size.description`:

Description
-----------

Calculates size of memory needed for structure \ ``p``\  followed by an
array of \ ``n``\  \ ``member``\  elements.

.. _`struct_size.return`:

Return
------

number of bytes needed or SIZE_MAX on overflow.

.. This file was automatic generated / don't edit.

