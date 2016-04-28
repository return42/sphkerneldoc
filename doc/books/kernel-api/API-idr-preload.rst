.. -*- coding: utf-8; mode: rst -*-

.. _API-idr-preload:

===========
idr_preload
===========

*man idr_preload(9)*

*4.6.0-rc5*

preload for ``idr_alloc``


Synopsis
========

.. c:function:: void idr_preload( gfp_t gfp_mask )

Arguments
=========

``gfp_mask``
    allocation mask to use for preloading


Description
===========

Preload per-cpu layer buffer for ``idr_alloc``. Can only be used from
process context and each ``idr_preload`` invocation should be matched
with ``idr_preload_end``. Note that preemption is disabled while
preloaded.

The first ``idr_alloc`` in the preloaded section can be treated as if it
were invoked with ``gfp_mask`` used for preloading. This allows using
more permissive allocation masks for idrs protected by spinlocks.

For example, if ``idr_alloc`` below fails, the failure can be treated as
if ``idr_alloc`` were called with GFP_KERNEL rather than GFP_NOWAIT.

idr_preload(GFP_KERNEL); spin_lock(lock);

id = idr_alloc(idr, ptr, start, end, GFP_NOWAIT);

spin_unlock(lock); ``idr_preload_end``; if (id < 0) error;


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
