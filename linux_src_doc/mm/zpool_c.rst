.. -*- coding: utf-8; mode: rst -*-
.. src-file: mm/zpool.c

.. _`zpool_register_driver`:

zpool_register_driver
=====================

.. c:function:: void zpool_register_driver(struct zpool_driver *driver)

    register a zpool implementation.

    :param struct zpool_driver \*driver:
        driver to register

.. _`zpool_unregister_driver`:

zpool_unregister_driver
=======================

.. c:function:: int zpool_unregister_driver(struct zpool_driver *driver)

    unregister a zpool implementation.

    :param struct zpool_driver \*driver:
        driver to unregister.

.. _`zpool_unregister_driver.description`:

Description
-----------

Module usage counting is used to prevent using a driver
while/after unloading, so if this is called from module
exit function, this should never fail; if called from
other than the module exit function, and this returns
failure, the driver is in use and must remain available.

.. _`zpool_has_pool`:

zpool_has_pool
==============

.. c:function:: bool zpool_has_pool(char *type)

    Check if the pool driver is available

    :param char \*type:
        The type of the zpool to check (e.g. zbud, zsmalloc)

.. _`zpool_has_pool.description`:

Description
-----------

This checks if the \ ``type``\  pool driver is available.  This will try to load
the requested module, if needed, but there is no guarantee the module will
still be loaded and available immediately after calling.  If this returns
true, the caller should assume the pool is available, but must be prepared
to handle the \ ``zpool_create_pool``\ () returning failure.  However if this
returns false, the caller should assume the requested pool type is not
available; either the requested pool type module does not exist, or could
not be loaded, and calling \ ``zpool_create_pool``\ () with the pool type will
fail.

The \ ``type``\  string must be null-terminated.

.. _`zpool_has_pool.return`:

Return
------

true if \ ``type``\  pool is available, false if not

.. _`zpool_create_pool`:

zpool_create_pool
=================

.. c:function:: struct zpool *zpool_create_pool(const char *type, const char *name, gfp_t gfp, const struct zpool_ops *ops)

    Create a new zpool

    :param const char \*type:
        The type of the zpool to create (e.g. zbud, zsmalloc)

    :param const char \*name:
        The name of the zpool (e.g. zram0, zswap)

    :param gfp_t gfp:
        The GFP flags to use when allocating the pool.

    :param const struct zpool_ops \*ops:
        The optional ops callback.

.. _`zpool_create_pool.description`:

Description
-----------

This creates a new zpool of the specified type.  The gfp flags will be
used when allocating memory, if the implementation supports it.  If the
ops param is NULL, then the created zpool will not be evictable.

Implementations must guarantee this to be thread-safe.

The \ ``type``\  and \ ``name``\  strings must be null-terminated.

.. _`zpool_create_pool.return`:

Return
------

New zpool on success, NULL on failure.

.. _`zpool_destroy_pool`:

zpool_destroy_pool
==================

.. c:function:: void zpool_destroy_pool(struct zpool *zpool)

    Destroy a zpool

    :param struct zpool \*zpool:
        The zpool to destroy.

.. _`zpool_destroy_pool.description`:

Description
-----------

Implementations must guarantee this to be thread-safe,
however only when destroying different pools.  The same
pool should only be destroyed once, and should not be used
after it is destroyed.

This destroys an existing zpool.  The zpool should not be in use.

.. _`zpool_get_type`:

zpool_get_type
==============

.. c:function:: const char *zpool_get_type(struct zpool *zpool)

    Get the type of the zpool

    :param struct zpool \*zpool:
        The zpool to check

.. _`zpool_get_type.description`:

Description
-----------

This returns the type of the pool.

Implementations must guarantee this to be thread-safe.

.. _`zpool_get_type.return`:

Return
------

The type of zpool.

.. _`zpool_malloc`:

zpool_malloc
============

.. c:function:: int zpool_malloc(struct zpool *zpool, size_t size, gfp_t gfp, unsigned long *handle)

    Allocate memory

    :param struct zpool \*zpool:
        The zpool to allocate from.

    :param size_t size:
        The amount of memory to allocate.

    :param gfp_t gfp:
        The GFP flags to use when allocating memory.

    :param unsigned long \*handle:
        Pointer to the handle to set

.. _`zpool_malloc.description`:

Description
-----------

This allocates the requested amount of memory from the pool.
The gfp flags will be used when allocating memory, if the
implementation supports it.  The provided \ ``handle``\  will be
set to the allocated object handle.

Implementations must guarantee this to be thread-safe.

.. _`zpool_malloc.return`:

Return
------

0 on success, negative value on error.

.. _`zpool_free`:

zpool_free
==========

.. c:function:: void zpool_free(struct zpool *zpool, unsigned long handle)

    Free previously allocated memory

    :param struct zpool \*zpool:
        The zpool that allocated the memory.

    :param unsigned long handle:
        The handle to the memory to free.

.. _`zpool_free.description`:

Description
-----------

This frees previously allocated memory.  This does not guarantee
that the pool will actually free memory, only that the memory
in the pool will become available for use by the pool.

Implementations must guarantee this to be thread-safe,
however only when freeing different handles.  The same
handle should only be freed once, and should not be used
after freeing.

.. _`zpool_shrink`:

zpool_shrink
============

.. c:function:: int zpool_shrink(struct zpool *zpool, unsigned int pages, unsigned int *reclaimed)

    Shrink the pool size

    :param struct zpool \*zpool:
        The zpool to shrink.

    :param unsigned int pages:
        The number of pages to shrink the pool.

    :param unsigned int \*reclaimed:
        The number of pages successfully evicted.

.. _`zpool_shrink.description`:

Description
-----------

This attempts to shrink the actual memory size of the pool
by evicting currently used handle(s).  If the pool was
created with no zpool_ops, or the evict call fails for any
of the handles, this will fail.  If non-NULL, the \ ``reclaimed``\ 
parameter will be set to the number of pages reclaimed,
which may be more than the number of pages requested.

Implementations must guarantee this to be thread-safe.

.. _`zpool_shrink.return`:

Return
------

0 on success, negative value on error/failure.

.. _`zpool_map_handle`:

zpool_map_handle
================

.. c:function:: void *zpool_map_handle(struct zpool *zpool, unsigned long handle, enum zpool_mapmode mapmode)

    Map a previously allocated handle into memory

    :param struct zpool \*zpool:
        The zpool that the handle was allocated from

    :param unsigned long handle:
        The handle to map

    :param enum zpool_mapmode mapmode:
        How the memory should be mapped

.. _`zpool_map_handle.description`:

Description
-----------

This maps a previously allocated handle into memory.  The \ ``mapmode``\ 
param indicates to the implementation how the memory will be
used, i.e. read-only, write-only, read-write.  If the
implementation does not support it, the memory will be treated
as read-write.

This may hold locks, disable interrupts, and/or preemption,
and the \ :c:func:`zpool_unmap_handle`\  must be called to undo those
actions.  The code that uses the mapped handle should complete
its operatons on the mapped handle memory quickly and unmap
as soon as possible.  As the implementation may use per-cpu
data, multiple handles should not be mapped concurrently on
any cpu.

.. _`zpool_map_handle.return`:

Return
------

A pointer to the handle's mapped memory area.

.. _`zpool_unmap_handle`:

zpool_unmap_handle
==================

.. c:function:: void zpool_unmap_handle(struct zpool *zpool, unsigned long handle)

    Unmap a previously mapped handle

    :param struct zpool \*zpool:
        The zpool that the handle was allocated from

    :param unsigned long handle:
        The handle to unmap

.. _`zpool_unmap_handle.description`:

Description
-----------

This unmaps a previously mapped handle.  Any locks or other
actions that the implementation took in \ :c:func:`zpool_map_handle`\ 
will be undone here.  The memory area returned from
\ :c:func:`zpool_map_handle`\  should no longer be used after this.

.. _`zpool_get_total_size`:

zpool_get_total_size
====================

.. c:function:: u64 zpool_get_total_size(struct zpool *zpool)

    The total size of the pool

    :param struct zpool \*zpool:
        The zpool to check

.. _`zpool_get_total_size.description`:

Description
-----------

This returns the total size in bytes of the pool.

.. _`zpool_get_total_size.return`:

Return
------

Total size of the zpool in bytes.

.. _`zpool_evictable`:

zpool_evictable
===============

.. c:function:: bool zpool_evictable(struct zpool *zpool)

    Test if zpool is potentially evictable

    :param struct zpool \*zpool:
        The zpool to test

.. _`zpool_evictable.description`:

Description
-----------

Zpool is only potentially evictable when it's created with struct
zpool_ops.evict and its driver implements struct zpool_driver.shrink.

However, it doesn't necessarily mean driver will use zpool_ops.evict
in its implementation of zpool_driver.shrink. It could do internal
defragmentation instead.

.. _`zpool_evictable.return`:

Return
------

true if potentially evictable; false otherwise.

.. This file was automatic generated / don't edit.

