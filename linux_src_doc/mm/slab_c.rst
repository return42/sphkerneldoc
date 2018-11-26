.. -*- coding: utf-8; mode: rst -*-
.. src-file: mm/slab.c

.. _`slab_destroy`:

slab_destroy
============

.. c:function:: void slab_destroy(struct kmem_cache *cachep, struct page *page)

    destroy and release all objects in a slab

    :param cachep:
        cache pointer being destroyed
    :type cachep: struct kmem_cache \*

    :param page:
        page pointer being destroyed
    :type page: struct page \*

.. _`slab_destroy.description`:

Description
-----------

Destroy all the objs in a slab page, and release the mem back to the system.
Before calling the slab page must have been unlinked from the cache. The
kmem_cache_node ->list_lock is not held/needed.

.. _`calculate_slab_order`:

calculate_slab_order
====================

.. c:function:: size_t calculate_slab_order(struct kmem_cache *cachep, size_t size, slab_flags_t flags)

    calculate size (page order) of slabs

    :param cachep:
        pointer to the cache that is being created
    :type cachep: struct kmem_cache \*

    :param size:
        size of objects to be created in this cache.
    :type size: size_t

    :param flags:
        slab allocation flags
    :type flags: slab_flags_t

.. _`calculate_slab_order.description`:

Description
-----------

Also calculates the number of objects per slab.

This could be made much more intelligent.  For now, try to avoid using
high order pages for slabs.  When the \ :c:func:`gfp`\  functions are more friendly
towards high-order requests, this should be changed.

.. _`__kmem_cache_create`:

__kmem_cache_create
===================

.. c:function:: int __kmem_cache_create(struct kmem_cache *cachep, slab_flags_t flags)

    Create a cache.

    :param cachep:
        cache management descriptor
    :type cachep: struct kmem_cache \*

    :param flags:
        SLAB flags
    :type flags: slab_flags_t

.. _`__kmem_cache_create.description`:

Description
-----------

Returns a ptr to the cache on success, NULL on failure.
Cannot be called within a int, but can be interrupted.
The \ ``ctor``\  is run when new pages are allocated by the cache.

The flags are

\ ``SLAB_POISON``\  - Poison the slab with a known test pattern (a5a5a5a5)
to catch references to uninitialised memory.

\ ``SLAB_RED_ZONE``\  - Insert `Red' zones around the allocated memory to check
for buffer overruns.

\ ``SLAB_HWCACHE_ALIGN``\  - Align the objects in this cache to a hardware
cacheline.  This can be beneficial if you're counting cycles as closely
as davem.

.. _`kmem_cache_alloc`:

kmem_cache_alloc
================

.. c:function:: void *kmem_cache_alloc(struct kmem_cache *cachep, gfp_t flags)

    Allocate an object

    :param cachep:
        The cache to allocate from.
    :type cachep: struct kmem_cache \*

    :param flags:
        See \ :c:func:`kmalloc`\ .
    :type flags: gfp_t

.. _`kmem_cache_alloc.description`:

Description
-----------

Allocate an object from this cache.  The flags are only relevant
if the cache has no available objects.

.. _`kmem_cache_alloc_node`:

kmem_cache_alloc_node
=====================

.. c:function:: void *kmem_cache_alloc_node(struct kmem_cache *cachep, gfp_t flags, int nodeid)

    Allocate an object on the specified node

    :param cachep:
        The cache to allocate from.
    :type cachep: struct kmem_cache \*

    :param flags:
        See \ :c:func:`kmalloc`\ .
    :type flags: gfp_t

    :param nodeid:
        node number of the target node.
    :type nodeid: int

.. _`kmem_cache_alloc_node.description`:

Description
-----------

Identical to kmem_cache_alloc but it will allocate memory on the given
node, which can improve the performance for cpu bound structures.

Fallback to other node is possible if __GFP_THISNODE is not set.

.. _`__do_kmalloc`:

__do_kmalloc
============

.. c:function:: void *__do_kmalloc(size_t size, gfp_t flags, unsigned long caller)

    allocate memory

    :param size:
        how many bytes of memory are required.
    :type size: size_t

    :param flags:
        the type of memory to allocate (see kmalloc).
    :type flags: gfp_t

    :param caller:
        function caller for debug tracking of the caller
    :type caller: unsigned long

.. _`kmem_cache_free`:

kmem_cache_free
===============

.. c:function:: void kmem_cache_free(struct kmem_cache *cachep, void *objp)

    Deallocate an object

    :param cachep:
        The cache the allocation was from.
    :type cachep: struct kmem_cache \*

    :param objp:
        The previously allocated object.
    :type objp: void \*

.. _`kmem_cache_free.description`:

Description
-----------

Free an object which was previously allocated from this
cache.

.. _`kfree`:

kfree
=====

.. c:function:: void kfree(const void *objp)

    free previously allocated memory

    :param objp:
        pointer returned by kmalloc.
    :type objp: const void \*

.. _`kfree.description`:

Description
-----------

If \ ``objp``\  is NULL, no operation is performed.

Don't free memory not originally allocated by \ :c:func:`kmalloc`\ 
or you will run into trouble.

.. _`cache_reap`:

cache_reap
==========

.. c:function:: void cache_reap(struct work_struct *w)

    Reclaim memory from caches.

    :param w:
        work descriptor
    :type w: struct work_struct \*

.. _`cache_reap.description`:

Description
-----------

Called from workqueue/eventd every few seconds.

.. _`cache_reap.purpose`:

Purpose
-------

- clear the per-cpu caches for this CPU.
- return freeable pages to the main free memory pool.

If we cannot acquire the cache chain mutex then just give up - we'll try
again on the next iteration.

.. _`slabinfo_write`:

slabinfo_write
==============

.. c:function:: ssize_t slabinfo_write(struct file *file, const char __user *buffer, size_t count, loff_t *ppos)

    Tuning for the slab allocator

    :param file:
        unused
    :type file: struct file \*

    :param buffer:
        user buffer
    :type buffer: const char __user \*

    :param count:
        data length
    :type count: size_t

    :param ppos:
        unused
    :type ppos: loff_t \*

.. _`ksize`:

ksize
=====

.. c:function:: size_t ksize(const void *objp)

    get the actual amount of memory allocated for a given object

    :param objp:
        Pointer to the object
    :type objp: const void \*

.. _`ksize.description`:

Description
-----------

kmalloc may internally round up allocations and return more memory
than requested. \ :c:func:`ksize`\  can be used to determine the actual amount of
memory allocated. The caller may use this additional memory, even though
a smaller amount of memory was initially specified with the kmalloc call.
The caller must guarantee that objp points to a valid object previously
allocated with either \ :c:func:`kmalloc`\  or \ :c:func:`kmem_cache_alloc`\ . The object
must not be freed during the duration of the call.

.. This file was automatic generated / don't edit.

