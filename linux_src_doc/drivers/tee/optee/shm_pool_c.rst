.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/tee/optee/shm_pool.c

.. _`optee_shm_pool_alloc_pages`:

optee_shm_pool_alloc_pages
==========================

.. c:function:: struct tee_shm_pool_mgr *optee_shm_pool_alloc_pages( void)

    create page-based allocator pool

    :param void:
        no arguments
    :type void: 

.. _`optee_shm_pool_alloc_pages.description`:

Description
-----------

This pool is used when OP-TEE supports dymanic SHM. In this case
command buffers and such are allocated from kernel's own memory.

.. This file was automatic generated / don't edit.

