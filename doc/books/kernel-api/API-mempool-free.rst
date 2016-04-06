
.. _API-mempool-free:

============
mempool_free
============

*man mempool_free(9)*

*4.6.0-rc1*

return an element to the pool.


Synopsis
========

.. c:function:: void mempool_free( void * element, mempool_t * pool )

Arguments
=========

``element``
    pool element pointer.

``pool``
    pointer to the memory pool which was allocated via ``mempool_create``.


Description
===========

this function only sleeps if the ``free_fn`` function sleeps.
