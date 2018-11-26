.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/include/asm/barrier.h

.. _`array_index_mask_nospec`:

array_index_mask_nospec
=======================

.. c:function:: unsigned long array_index_mask_nospec(unsigned long index, unsigned long size)

    generate a mask that is ~0UL when the bounds check succeeds and 0 otherwise

    :param index:
        array element index
    :type index: unsigned long

    :param size:
        number of elements in array
    :type size: unsigned long

.. _`array_index_mask_nospec.return`:

Return
------

0 - (index < size)

.. This file was automatic generated / don't edit.

