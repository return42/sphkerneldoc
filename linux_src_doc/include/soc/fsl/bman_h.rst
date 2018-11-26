.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/soc/fsl/bman.h

.. _`bman_new_pool`:

bman_new_pool
=============

.. c:function:: struct bman_pool *bman_new_pool( void)

    Allocates a Buffer Pool object

    :param void:
        no arguments
    :type void: 

.. _`bman_new_pool.description`:

Description
-----------

Creates a pool object, and returns a reference to it or NULL on error.

.. _`bman_free_pool`:

bman_free_pool
==============

.. c:function:: void bman_free_pool(struct bman_pool *pool)

    Deallocates a Buffer Pool object

    :param pool:
        the pool object to release
    :type pool: struct bman_pool \*

.. _`bman_get_bpid`:

bman_get_bpid
=============

.. c:function:: int bman_get_bpid(const struct bman_pool *pool)

    Returns a pool object's BPID.

    :param pool:
        the pool object
    :type pool: const struct bman_pool \*

.. _`bman_get_bpid.description`:

Description
-----------

The returned value is the index of the encapsulated buffer pool,
in the range of [0, \ ``BM_POOL_MAX``\ -1].

.. _`bman_release`:

bman_release
============

.. c:function:: int bman_release(struct bman_pool *pool, const struct bm_buffer *bufs, u8 num)

    Release buffer(s) to the buffer pool

    :param pool:
        the buffer pool object to release to
    :type pool: struct bman_pool \*

    :param bufs:
        an array of buffers to release
    :type bufs: const struct bm_buffer \*

    :param num:
        the number of buffers in \ ``bufs``\  (1-8)
    :type num: u8

.. _`bman_release.description`:

Description
-----------

Adds the given buffers to RCR entries. If the RCR ring is unresponsive,
the function will return -ETIMEDOUT. Otherwise, it returns zero.

.. _`bman_acquire`:

bman_acquire
============

.. c:function:: int bman_acquire(struct bman_pool *pool, struct bm_buffer *bufs, u8 num)

    Acquire buffer(s) from a buffer pool

    :param pool:
        the buffer pool object to acquire from
    :type pool: struct bman_pool \*

    :param bufs:
        array for storing the acquired buffers
    :type bufs: struct bm_buffer \*

    :param num:
        the number of buffers desired (@bufs is at least this big)
    :type num: u8

.. _`bman_acquire.description`:

Description
-----------

Issues an "Acquire" command via the portal's management command interface.
The return value will be the number of buffers obtained from the pool, or a
negative error code if a h/w error or pool starvation was encountered. In
the latter case, the content of \ ``bufs``\  is undefined.

.. _`bman_is_probed`:

bman_is_probed
==============

.. c:function:: int bman_is_probed( void)

    Check if bman is probed

    :param void:
        no arguments
    :type void: 

.. _`bman_is_probed.description`:

Description
-----------

Returns 1 if the bman driver successfully probed, -1 if the bman driver
failed to probe or 0 if the bman driver did not probed yet.

.. This file was automatic generated / don't edit.

