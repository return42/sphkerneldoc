.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/include/asm/barrier.h

.. _`array_index_mask_nospec`:

array_index_mask_nospec
=======================

.. c:function:: unsigned long array_index_mask_nospec(unsigned long index, unsigned long size)

    generate a mask that is ~0UL when the bounds check succeeds and 0 otherwise

    :param unsigned long index:
        array element index

    :param unsigned long size:
        number of elements in array

.. _`array_index_mask_nospec.return`:

Return
------

0 - (index < size)

.. This file was automatic generated / don't edit.

