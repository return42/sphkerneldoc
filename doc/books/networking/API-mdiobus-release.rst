
.. _API-mdiobus-release:

===============
mdiobus_release
===============

*man mdiobus_release(9)*

*4.6.0-rc1*

mii_bus device release callback


Synopsis
========

.. c:function:: void mdiobus_release( struct device * d )

Arguments
=========

``d``
    the target struct device that contains the mii_bus


Description
===========

called when the last reference to an mii_bus is dropped, to free the underlying memory.
