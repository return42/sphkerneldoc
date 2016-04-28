.. -*- coding: utf-8; mode: rst -*-

.. _API-mdiobus-alloc-size:

==================
mdiobus_alloc_size
==================

*man mdiobus_alloc_size(9)*

*4.6.0-rc5*

allocate a mii_bus structure


Synopsis
========

.. c:function:: struct mii_bus * mdiobus_alloc_size( size_t size )

Arguments
=========

``size``
    extra amount of memory to allocate for private storage. If non-zero,
    then bus->priv is points to that memory.


Description
===========

called by a bus driver to allocate an mii_bus structure to fill in.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
