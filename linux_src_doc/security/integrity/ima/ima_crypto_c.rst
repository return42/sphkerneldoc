.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/integrity/ima/ima_crypto.c

.. _`ima_alloc_pages`:

ima_alloc_pages
===============

.. c:function:: void *ima_alloc_pages(loff_t max_size, size_t *allocated_size, int last_warn)

    Allocate contiguous pages.

    :param max_size:
        Maximum amount of memory to allocate.
    :type max_size: loff_t

    :param allocated_size:
        Returned size of actual allocation.
    :type allocated_size: size_t \*

    :param last_warn:
        Should the min_size allocation warn or not.
    :type last_warn: int

.. _`ima_alloc_pages.description`:

Description
-----------

Tries to do opportunistic allocation for memory first trying to allocate
max_size amount of memory and then splitting that until zero order is
reached. Allocation is tried without generating allocation warnings unless
last_warn is set. Last_warn set affects only last allocation of zero order.

By default, ima_maxorder is 0 and it is equivalent to kmalloc(GFP_KERNEL)

Return pointer to allocated memory, or NULL on failure.

.. _`ima_free_pages`:

ima_free_pages
==============

.. c:function:: void ima_free_pages(void *ptr, size_t size)

    Free pages allocated by \ :c:func:`ima_alloc_pages`\ .

    :param ptr:
        Pointer to allocated pages.
    :type ptr: void \*

    :param size:
        Size of allocated buffer.
    :type size: size_t

.. This file was automatic generated / don't edit.

