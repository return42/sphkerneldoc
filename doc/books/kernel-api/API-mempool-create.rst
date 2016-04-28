.. -*- coding: utf-8; mode: rst -*-

.. _API-mempool-create:

==============
mempool_create
==============

*man mempool_create(9)*

*4.6.0-rc5*

create a memory pool


Synopsis
========

.. c:function:: mempool_t * mempool_create( int min_nr, mempool_alloc_t * alloc_fn, mempool_free_t * free_fn, void * pool_data )

Arguments
=========

``min_nr``
    the minimum number of elements guaranteed to be allocated for this
    pool.

``alloc_fn``
    user-defined element-allocation function.

``free_fn``
    user-defined element-freeing function.

``pool_data``
    optional private data available to the user-defined functions.


Description
===========

this function creates and allocates a guaranteed size, preallocated
memory pool. The pool can be used from the ``mempool_alloc`` and
``mempool_free`` functions. This function might sleep. Both the
``alloc_fn`` and the ``free_fn`` functions might sleep - as long as the
``mempool_alloc`` function is not called from IRQ contexts.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
