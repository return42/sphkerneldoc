
.. _API-mdiobus-free:

============
mdiobus_free
============

*man mdiobus_free(9)*

*4.6.0-rc1*

free a struct mii_bus


Synopsis
========

.. c:function:: void mdiobus_free( struct mii_bus * bus )

Arguments
=========

``bus``
    mii_bus to free


Description
===========

This function releases the reference to the underlying device object in the mii_bus. If this is the last reference, the mii_bus will be freed.
