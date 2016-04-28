.. -*- coding: utf-8; mode: rst -*-

.. _API-devm-mdiobus-free:

=================
devm_mdiobus_free
=================

*man devm_mdiobus_free(9)*

*4.6.0-rc5*

Resource-managed ``mdiobus_free``


Synopsis
========

.. c:function:: void devm_mdiobus_free( struct device * dev, struct mii_bus * bus )

Arguments
=========

``dev``
    Device this mii_bus belongs to

``bus``
    the mii_bus associated with the device


Description
===========

Free mii_bus allocated with ``devm_mdiobus_alloc_size``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
