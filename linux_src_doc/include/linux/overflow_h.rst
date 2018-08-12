.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/overflow.h

.. _`array_size`:

array_size
==========

.. c:function:: size_t array_size(size_t a, size_t b)

    Calculate size of 2-dimensional array.

    :param size_t a:
        dimension one

    :param size_t b:
        dimension two

.. _`array_size.description`:

Description
-----------

Calculates size of 2-dimensional array: \ ``a``\  \* \ ``b``\ .

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

    :param size_t a:
        dimension one

    :param size_t b:
        dimension two

    :param size_t c:
        dimension three

.. _`array3_size.description`:

Description
-----------

Calculates size of 3-dimensional array: \ ``a``\  \* \ ``b``\  \* \ ``c``\ .

.. _`array3_size.return`:

Return
------

number of bytes needed to represent the array or SIZE_MAX on
overflow.

.. This file was automatic generated / don't edit.

