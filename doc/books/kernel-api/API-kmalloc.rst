
.. _API-kmalloc:

=======
kmalloc
=======

*man kmalloc(9)*

*4.6.0-rc1*

allocate memory


Synopsis
========

.. c:function:: void ⋆ kmalloc( size_t size, gfp_t flags )

Arguments
=========

``size``
    how many bytes of memory are required.

``flags``
    the type of memory to allocate.


Description
===========

kmalloc is the normal method of allocating memory for objects smaller than page size in the kernel.

The ``flags`` argument may be one of:

``GFP_USER`` - Allocate memory on behalf of user. May sleep.

``GFP_KERNEL`` - Allocate normal kernel ram. May sleep.

``GFP_ATOMIC`` - Allocation will not sleep. May use emergency pools. For example, use this inside interrupt handlers.

``GFP_HIGHUSER`` - Allocate pages from high memory.

``GFP_NOIO`` - Do not do any I/O at all while trying to get memory.

``GFP_NOFS`` - Do not make any fs calls while trying to get memory.

``GFP_NOWAIT`` - Allocation will not sleep.

``__GFP_THISNODE`` - Allocate node-local memory only.

``GFP_DMA`` - Allocation suitable for DMA. Should only be used for ``kmalloc`` caches. Otherwise, use a slab created with SLAB_DMA.

Also it is possible to set different flags by OR'ing in one or more of the following additional ``flags``:

``__GFP_COLD`` - Request cache-cold pages instead of trying to return cache-warm pages.

``__GFP_HIGH`` - This allocation has high priority and may use emergency pools.

``__GFP_NOFAIL`` - Indicate that this allocation is in no way allowed to fail (think twice before using).

``__GFP_NORETRY`` - If memory is not immediately available, then give up at once.

``__GFP_NOWARN`` - If allocation fails, don't issue any warnings.

``__GFP_REPEAT`` - If allocation fails initially, try once more before failing.

There are other flags available as well, but these are not intended for general use, and so are not documented here. For a full list of potential flags, always refer to
linux/gfp.h.
