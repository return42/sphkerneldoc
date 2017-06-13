.. -*- coding: utf-8; mode: rst -*-
.. src-file: mm/slab_common.c

.. _`slab_deactivate_memcg_cache_rcu_sched`:

slab_deactivate_memcg_cache_rcu_sched
=====================================

.. c:function:: void slab_deactivate_memcg_cache_rcu_sched(struct kmem_cache *s, void (*deact_fn)(struct kmem_cache *))

    schedule deactivation after a sched RCU grace period

    :param struct kmem_cache \*s:
        target kmem_cache

    :param void (\*deact_fn)(struct kmem_cache \*):
        deactivation function to call

.. _`slab_deactivate_memcg_cache_rcu_sched.description`:

Description
-----------

Schedule \ ``deact_fn``\  to be invoked with online cpus, mems and slab_mutex
held after a sched RCU grace period.  The slab is guaranteed to stay
alive until \ ``deact_fn``\  is finished.  This is to be used from
\__kmemcg_cache_deactivate().

.. _`kmem_cache_shrink`:

kmem_cache_shrink
=================

.. c:function:: int kmem_cache_shrink(struct kmem_cache *cachep)

    Shrink a cache.

    :param struct kmem_cache \*cachep:
        The cache to shrink.

.. _`kmem_cache_shrink.description`:

Description
-----------

Releases as many slabs as possible for a cache.
To help debugging, a zero exit status indicates all slabs were released.

.. _`__krealloc`:

__krealloc
==========

.. c:function:: void *__krealloc(const void *p, size_t new_size, gfp_t flags)

    like \ :c:func:`krealloc`\  but don't free \ ``p``\ .

    :param const void \*p:
        object to reallocate memory for.

    :param size_t new_size:
        how many bytes of memory are required.

    :param gfp_t flags:
        the type of memory to allocate.

.. _`__krealloc.description`:

Description
-----------

This function is like \ :c:func:`krealloc`\  except it never frees the originally
allocated buffer. Use this if you don't want to free the buffer immediately
like, for example, with RCU.

.. _`krealloc`:

krealloc
========

.. c:function:: void *krealloc(const void *p, size_t new_size, gfp_t flags)

    reallocate memory. The contents will remain unchanged.

    :param const void \*p:
        object to reallocate memory for.

    :param size_t new_size:
        how many bytes of memory are required.

    :param gfp_t flags:
        the type of memory to allocate.

.. _`krealloc.description`:

Description
-----------

The contents of the object pointed to are preserved up to the
lesser of the new and old sizes.  If \ ``p``\  is \ ``NULL``\ , \ :c:func:`krealloc`\ 
behaves exactly like \ :c:func:`kmalloc`\ .  If \ ``new_size``\  is 0 and \ ``p``\  is not a
\ ``NULL``\  pointer, the object pointed to is freed.

.. _`kzfree`:

kzfree
======

.. c:function:: void kzfree(const void *p)

    like kfree but zero memory

    :param const void \*p:
        object to free memory of

.. _`kzfree.description`:

Description
-----------

The memory of the object \ ``p``\  points to is zeroed before freed.
If \ ``p``\  is \ ``NULL``\ , \ :c:func:`kzfree`\  does nothing.

.. _`kzfree.note`:

Note
----

this function zeroes the whole allocated buffer which can be a good
deal bigger than the requested buffer size passed to \ :c:func:`kmalloc`\ . So be
careful when using this function in performance sensitive code.

.. This file was automatic generated / don't edit.

