.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/include/asm/octeon/cvmx-fpa.h

.. _`cvmx_fpa_iobdma_data_t`:

typedef cvmx_fpa_iobdma_data_t
==============================

.. c:type:: typedef cvmx_fpa_iobdma_data_t


.. _`cvmx_fpa_pool_info_t`:

typedef cvmx_fpa_pool_info_t
============================

.. c:type:: typedef cvmx_fpa_pool_info_t


.. _`cvmx_fpa_get_name`:

cvmx_fpa_get_name
=================

.. c:function:: const char *cvmx_fpa_get_name(uint64_t pool)

    :param pool:
        Pool to get the name of
        Returns The name
    :type pool: uint64_t

.. _`cvmx_fpa_get_base`:

cvmx_fpa_get_base
=================

.. c:function:: void *cvmx_fpa_get_base(uint64_t pool)

    :param pool:
        Pool to get the base of
        Returns The base
    :type pool: uint64_t

.. _`cvmx_fpa_is_member`:

cvmx_fpa_is_member
==================

.. c:function:: int cvmx_fpa_is_member(uint64_t pool, void *ptr)

    zero if the supplied pointer is inside the memory controlled by an FPA pool.

    :param pool:
        Pool to check
    :type pool: uint64_t

    :param ptr:
        Pointer to check
        Returns Non-zero if pointer is in the pool. Zero if not
    :type ptr: void \*

.. _`cvmx_fpa_enable`:

cvmx_fpa_enable
===============

.. c:function:: void cvmx_fpa_enable( void)

    configuration but before any other FPA functions.

    :param void:
        no arguments
    :type void: 

.. _`cvmx_fpa_alloc`:

cvmx_fpa_alloc
==============

.. c:function:: void *cvmx_fpa_alloc(uint64_t pool)

    :param pool:
        Pool to get the block from
        Returns Pointer to the block or NULL on failure
    :type pool: uint64_t

.. _`cvmx_fpa_async_alloc`:

cvmx_fpa_async_alloc
====================

.. c:function:: void cvmx_fpa_async_alloc(uint64_t scr_addr, uint64_t pool)

    :param scr_addr:
        Local scratch address to put response in.  This is a byte address,
        but must be 8 byte aligned.
    :type scr_addr: uint64_t

    :param pool:
        Pool to get the block from
    :type pool: uint64_t

.. _`cvmx_fpa_free_nosync`:

cvmx_fpa_free_nosync
====================

.. c:function:: void cvmx_fpa_free_nosync(void *ptr, uint64_t pool, uint64_t num_cache_lines)

    ordering in cases where the memory block was modified by the core.

    :param ptr:
        Block to free
    :type ptr: void \*

    :param pool:
        Pool to put it in
    :type pool: uint64_t

    :param num_cache_lines:
        Cache lines to invalidate
    :type num_cache_lines: uint64_t

.. _`cvmx_fpa_free`:

cvmx_fpa_free
=============

.. c:function:: void cvmx_fpa_free(void *ptr, uint64_t pool, uint64_t num_cache_lines)

    ordering in cases where memory block was modified by core.

    :param ptr:
        Block to free
    :type ptr: void \*

    :param pool:
        Pool to put it in
    :type pool: uint64_t

    :param num_cache_lines:
        Cache lines to invalidate
    :type num_cache_lines: uint64_t

.. _`cvmx_fpa_setup_pool`:

cvmx_fpa_setup_pool
===================

.. c:function:: int cvmx_fpa_setup_pool(uint64_t pool, const char *name, void *buffer, uint64_t block_size, uint64_t num_blocks)

    This can only be called once per pool. Make sure proper locking enforces this.

    :param pool:
        Pool to initialize
        0 <= pool < 8
    :type pool: uint64_t

    :param name:
        Constant character string to name this pool.
        String is not copied.
    :type name: const char \*

    :param buffer:
        Pointer to the block of memory to use. This must be
        accessible by all processors and external hardware.
    :type buffer: void \*

    :param block_size:
        Size for each block controlled by the FPA
    :type block_size: uint64_t

    :param num_blocks:
        Number of blocks
    :type num_blocks: uint64_t

.. _`cvmx_fpa_setup_pool.description`:

Description
-----------

Returns 0 on Success,
-1 on failure

.. _`cvmx_fpa_shutdown_pool`:

cvmx_fpa_shutdown_pool
======================

.. c:function:: uint64_t cvmx_fpa_shutdown_pool(uint64_t pool)

    the buffers originally placed in it. This should only be called by one processor after all hardware has finished using the pool.

    :param pool:
        Pool to shutdown
        Returns Zero on success
        - Positive is count of missing buffers
        - Negative is too many buffers or corrupted pointers
    :type pool: uint64_t

.. _`cvmx_fpa_get_block_size`:

cvmx_fpa_get_block_size
=======================

.. c:function:: uint64_t cvmx_fpa_get_block_size(uint64_t pool)

    This is resolved to a constant at compile time.

    :param pool:
        Pool to access
        Returns Size of the block in bytes
    :type pool: uint64_t

.. This file was automatic generated / don't edit.

