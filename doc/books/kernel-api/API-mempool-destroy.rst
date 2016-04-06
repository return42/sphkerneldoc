
.. _API-mempool-destroy:

===============
mempool_destroy
===============

*man mempool_destroy(9)*

*4.6.0-rc1*

deallocate a memory pool


Synopsis
========

.. c:function:: void mempool_destroy( mempool_t * pool )

Arguments
=========

``pool``
    pointer to the memory pool which was allocated via ``mempool_create``.


Description
===========

Free all reserved elements in ``pool`` and ``pool`` itself. This function only sleeps if the ``free_fn`` function sleeps.
