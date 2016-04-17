.. -*- coding: utf-8; mode: rst -*-

=======
zpool.h
=======


.. _`zpool_driver`:

struct zpool_driver
===================

.. c:type:: zpool_driver

    driver implementation for zpool


.. _`zpool_driver.definition`:

Definition
----------

.. code-block:: c

  struct zpool_driver {
    char * type;
    struct list_head list;
    void *(* create) (const char *name,gfp_t gfp,const struct zpool_ops *ops,struct zpool *zpool);
    void (* destroy) (void *pool);
    int (* malloc) (void *pool, size_t size, gfp_t gfp,unsigned long *handle);
    void (* free) (void *pool, unsigned long handle);
    int (* shrink) (void *pool, unsigned int pages,unsigned int *reclaimed);
    void *(* map) (void *pool, unsigned long handle,enum zpool_mapmode mm);
    void (* unmap) (void *pool, unsigned long handle);
    u64 (* total_size) (void *pool);
  };


.. _`zpool_driver.members`:

Members
-------

:``type``:
    name of the driver.

:``list``:
    entry in the list of zpool drivers.

:``create``:
    create a new pool.

:``destroy``:
    destroy a pool.

:``malloc``:
    allocate mem from a pool.

:``free``:
    free mem from a pool.

:``shrink``:
    shrink the pool.

:``map``:
    map a handle.

:``unmap``:
    unmap a handle.

:``total_size``:
    get total size of a pool.




.. _`zpool_driver.description`:

Description
-----------

This is created by a zpool implementation and registered
with zpool.

