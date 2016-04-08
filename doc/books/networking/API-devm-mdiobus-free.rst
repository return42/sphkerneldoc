
.. _API-devm-mdiobus-free:

=================
devm_mdiobus_free
=================

*man devm_mdiobus_free(9)*

*4.6.0-rc1*

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
