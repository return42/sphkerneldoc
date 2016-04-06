
.. _API-relay-alloc-buf:

===============
relay_alloc_buf
===============

*man relay_alloc_buf(9)*

*4.6.0-rc1*

allocate a channel buffer


Synopsis
========

.. c:function:: void ⋆ relay_alloc_buf( struct rchan_buf * buf, size_t * size )

Arguments
=========

``buf``
    the buffer struct

``size``
    total size of the buffer


Description
===========

Returns a pointer to the resulting buffer, ``NULL`` if unsuccessful. The passed in size will get page aligned, if it isn't already.
