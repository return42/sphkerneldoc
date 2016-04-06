
.. _API-kmemdup:

=======
kmemdup
=======

*man kmemdup(9)*

*4.6.0-rc1*

duplicate region of memory


Synopsis
========

.. c:function:: void ⋆ kmemdup( const void * src, size_t len, gfp_t gfp )

Arguments
=========

``src``
    memory region to duplicate

``len``
    memory region length

``gfp``
    GFP mask to use
