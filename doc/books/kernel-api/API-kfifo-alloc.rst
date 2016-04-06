
.. _API-kfifo-alloc:

===========
kfifo_alloc
===========

*man kfifo_alloc(9)*

*4.6.0-rc1*

dynamically allocates a new fifo buffer


Synopsis
========

.. c:function:: kfifo_alloc( fifo, size, gfp_mask )

Arguments
=========

``fifo``
    pointer to the fifo

``size``
    the number of elements in the fifo, this must be a power of 2

``gfp_mask``
    get_free_pages mask, passed to ``kmalloc``


Description
===========

This macro dynamically allocates a new fifo buffer.

The numer of elements will be rounded-up to a power of 2. The fifo will be release with ``kfifo_free``. Return 0 if no error, otherwise an error code.
