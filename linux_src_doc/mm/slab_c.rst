.. -*- coding: utf-8; mode: rst -*-
.. src-file: mm/slab.c

.. _`slab_destroy`:

slab_destroy
============

.. c:function:: void slab_destroy(struct kmem_cache *cachep, struct page *page)

    destroy and release all objects in a slab

    :param struct kmem_cache \*cachep:
        cache pointer being destroyed

    :param struct page \*page:
        page pointer being destroyed

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

    :param struct kmem_cache \*cachep:
        pointer to the cache that is being created

    :param size_t size:
        size of objects to be created in this cache.

    :param slab_flags_t flags:
        slab allocation flags

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

    :param struct kmem_cache \*cachep:
        cache management descriptor

    :param slab_flags_t flags:
        SLAB flags

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

    :param struct kmem_cache \*cachep:
        The cache to allocate from.

    :param gfp_t flags:
        See \ :c:func:`kmalloc`\ .

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

    :param struct kmem_cache \*cachep:
        The cache to allocate from.

    :param gfp_t flags:
        See \ :c:func:`kmalloc`\ .

    :param int nodeid:
        node number of the target node.

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

    :param size_t size:
        how many bytes of memory are required.

    :param gfp_t flags:
        the type of memory to allocate (see kmalloc).

    :param unsigned long caller:
        function caller for debug tracking of the caller

.. _`kmem_cache_free`:

kmem_cache_free
===============

.. c:function:: void kmem_cache_free(struct kmem_cache *cachep, void *objp)

    Deallocate an object

    :param struct kmem_cache \*cachep:
        The cache the allocation was from.

    :param void \*objp:
        The previously allocated object.

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

    :param const void \*objp:
        pointer returned by kmalloc.

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

    :param struct work_struct \*w:
        work descriptor

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

    :param struct file \*file:
        unused

    :param const char __user \*buffer:
        user buffer

    :param size_t count:
        data length

    :param loff_t \*ppos:
        unused

.. _`ksize`:

ksize
=====

.. c:function:: size_t ksize(const void *objp)

    get the actual amount of memory allocated for a given object

    :param const void \*objp:
        Pointer to the object

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

