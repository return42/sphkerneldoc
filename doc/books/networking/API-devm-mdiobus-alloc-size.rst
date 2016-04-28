.. -*- coding: utf-8; mode: rst -*-

.. _API-devm-mdiobus-alloc-size:

=======================
devm_mdiobus_alloc_size
=======================

*man devm_mdiobus_alloc_size(9)*

*4.6.0-rc5*

Resource-managed ``mdiobus_alloc_size``


Synopsis
========

.. c:function:: struct mii_bus * devm_mdiobus_alloc_size( struct device * dev, int sizeof_priv )

Arguments
=========

``dev``
    Device to allocate mii_bus for

``sizeof_priv``
    Space to allocate for private structure.


Description
===========

Managed mdiobus_alloc_size. mii_bus allocated with this function is
automatically freed on driver detach.

If an mii_bus allocated with this function needs to be freed
separately, ``devm_mdiobus_free`` must be used.


RETURNS
=======

Pointer to allocated mii_bus on success, NULL on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
