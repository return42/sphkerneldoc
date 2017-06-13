.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/tee/tee_shm_pool.c

.. _`tee_shm_pool_alloc_res_mem`:

tee_shm_pool_alloc_res_mem
==========================

.. c:function:: struct tee_shm_pool *tee_shm_pool_alloc_res_mem(struct tee_shm_pool_mem_info *priv_info, struct tee_shm_pool_mem_info *dmabuf_info)

    Create a shared memory pool from reserved memory range

    :param struct tee_shm_pool_mem_info \*priv_info:
        Information for driver private shared memory pool

    :param struct tee_shm_pool_mem_info \*dmabuf_info:
        Information for dma-buf shared memory pool

.. _`tee_shm_pool_alloc_res_mem.description`:

Description
-----------

Start and end of pools will must be page aligned.

Allocation with the flag TEE_SHM_DMA_BUF set will use the range supplied
in \ ``dmabuf``\ , others will use the range provided by \ ``priv``\ .

\ ``returns``\  pointer to a 'struct tee_shm_pool' or an ERR_PTR on failure.

.. _`tee_shm_pool_free`:

tee_shm_pool_free
=================

.. c:function:: void tee_shm_pool_free(struct tee_shm_pool *pool)

    Free a shared memory pool

    :param struct tee_shm_pool \*pool:
        The shared memory pool to free

.. _`tee_shm_pool_free.description`:

Description
-----------

There must be no remaining shared memory allocated from this pool when
this function is called.

.. This file was automatic generated / don't edit.

