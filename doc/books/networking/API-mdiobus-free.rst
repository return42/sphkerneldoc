.. -*- coding: utf-8; mode: rst -*-

.. _API-mdiobus-free:

============
mdiobus_free
============

*man mdiobus_free(9)*

*4.6.0-rc5*

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

This function releases the reference to the underlying device object in
the mii_bus. If this is the last reference, the mii_bus will be freed.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
