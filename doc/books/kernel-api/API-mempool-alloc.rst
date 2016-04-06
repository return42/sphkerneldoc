
.. _API-mempool-alloc:

=============
mempool_alloc
=============

*man mempool_alloc(9)*

*4.6.0-rc1*

allocate an element from a specific memory pool


Synopsis
========

.. c:function:: void ⋆ mempool_alloc( mempool_t * pool, gfp_t gfp_mask )

Arguments
=========

``pool``
    pointer to the memory pool which was allocated via ``mempool_create``.

``gfp_mask``
    the usual allocation bitmask.


Description
===========

this function only sleeps if the ``alloc_fn`` function sleeps or returns NULL. Note that due to preallocation, this function ⋆never⋆ fails when called from process contexts. (it
might fail if called from an IRQ context.)


Note
====

neither __GFP_NOMEMALLOC nor __GFP_ZERO are supported.
