
.. _API-mdiobus-alloc-size:

==================
mdiobus_alloc_size
==================

*man mdiobus_alloc_size(9)*

*4.6.0-rc1*

allocate a mii_bus structure


Synopsis
========

.. c:function:: struct mii_bus ⋆ mdiobus_alloc_size( size_t size )

Arguments
=========

``size``
    extra amount of memory to allocate for private storage. If non-zero, then bus->priv is points to that memory.


Description
===========

called by a bus driver to allocate an mii_bus structure to fill in.
