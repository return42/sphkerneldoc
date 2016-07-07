.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/sort.c

.. _`sort`:

sort
====

.. c:function:: void sort(void *base, size_t num, size_t size, int (*) cmp_func (const void *, const void *, void (*) swap_func (void *, void *, int size)

    sort an array of elements

    :param void \*base:
        pointer to data to sort

    :param size_t num:
        number of elements

    :param size_t size:
        size of each element

    :param (int (\*) cmp_func (const void \*, const void \*):
        pointer to comparison function

    :param (void (\*) swap_func (void \*, void \*, int size):
        pointer to swap function or NULL

.. _`sort.description`:

Description
-----------

This function does a heapsort on the given array. You may provide a
swap_func function optimized to your element type.

Sorting time is O(n log n) both on average and worst-case. While
qsort is about 20% faster on average, it suffers from exploitable
O(n\*n) worst-case behavior and extra memory requirements that make
it less suitable for kernel use.

.. This file was automatic generated / don't edit.

