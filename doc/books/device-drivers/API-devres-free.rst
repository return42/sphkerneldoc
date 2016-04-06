
.. _API-devres-free:

===========
devres_free
===========

*man devres_free(9)*

*4.6.0-rc1*

Free device resource data


Synopsis
========

.. c:function:: void devres_free( void * res )

Arguments
=========

``res``
    Pointer to devres data to free


Description
===========

Free devres created with ``devres_alloc``.
