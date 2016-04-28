.. -*- coding: utf-8; mode: rst -*-

.. _API-mempool-resize:

==============
mempool_resize
==============

*man mempool_resize(9)*

*4.6.0-rc5*

resize an existing memory pool


Synopsis
========

.. c:function:: int mempool_resize( mempool_t * pool, int new_min_nr )

Arguments
=========

``pool``
    pointer to the memory pool which was allocated via
    ``mempool_create``.

``new_min_nr``
    the new minimum number of elements guaranteed to be allocated for
    this pool.


Description
===========

This function shrinks/grows the pool. In the case of growing, it cannot
be guaranteed that the pool will be grown to the new size immediately,
but new ``mempool_free`` calls will refill it. This function may sleep.

Note, the caller must guarantee that no mempool_destroy is called while
this function is running. ``mempool_alloc`` & ``mempool_free`` might be
called (eg. from IRQ contexts) while this function executes.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
