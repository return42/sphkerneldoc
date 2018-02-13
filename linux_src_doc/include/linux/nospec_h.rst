.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/nospec.h

.. _`array_index_mask_nospec`:

array_index_mask_nospec
=======================

.. c:function:: unsigned long array_index_mask_nospec(unsigned long index, unsigned long size)

    generate a ~0 mask when index < size, 0 otherwise

    :param unsigned long index:
        array element index

    :param unsigned long size:
        number of elements in array

.. _`array_index_mask_nospec.description`:

Description
-----------

When \ ``index``\  is out of bounds (@index >= \ ``size``\ ), the sign bit will be
set.  Extend the sign bit to all bits and invert, giving a result of
zero for an out of bounds index, or ~0 if within bounds [0, \ ``size``\ ).

.. This file was automatic generated / don't edit.

